#one doc.
def DecodeBlog(data) -> dict:
    return {
        'id' : str(data['_id']),
        'title' : data['title'],
        'subtitle' : data['subtitle'],
        'body' : data['body'],
        'author' : data['author'],
        'published' : data['published'],
        'date' : data['date'],
    }
        
def DecodeBlogs(data) -> list:
    return [DecodeBlog(blog) for blog in data]   
    