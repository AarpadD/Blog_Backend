from fastapi import APIRouter
from models.blog import Blog, UpdateBlog
from config.config import blogs_collection  
from serializers.blog import DecodeBlog, DecodeBlogs
import datetime 
from bson import ObjectId


blog_root = APIRouter()

#post reuqest
@blog_root.post("/new/blog")
def new_blog(data: Blog):
    data = dict(data)
    current_date = datetime.date.today()
    data["date"] = str(current_date)
    
    res = blogs_collection.insert_one(data)
    data_id = str(res.inserted_id)
    
    return {
        "status": "ok",
        "message": "Blog added successfully",
        "_id": data_id
    }

   
#get request
@blog_root.get("/all/blogs")
def AllBlogs():
    res = blogs_collection.find()
    decoded_data = DecodeBlogs(res)
    
    return {
        'status': 'ok',
        'data': decoded_data
    }
    
@blog_root.get("/blog/{_id}")
def GetBlog(_id:str) :
    res = blogs_collection.find_one({"_id": ObjectId(_id)})
    decoded_blog = DecodeBlog(res)
    return {
        'status': 'ok',
        'data': decoded_blog
    }


#update request  
@blog_root.patch("/update/{_id}")
def UpdateBlog(_id:str, doc:UpdateBlog):
    req = dict(doc.model_dump(exclude_unset=True))
    blogs_collection.find_one_and_update({"_id": ObjectId(_id)}, {"$set": req})
    return {
        "status": "ok",
        "message": "Blog updated successfully"
    }
    

#delete request
@blog_root.delete("/delete/{_id}")
def DeleteBlog(_id:str):
    blogs_collection.find_one_and_delete({"_id": ObjectId(_id)})
    return {
        "status": "ok",
        "message": "Blog deleted successfully"
    }