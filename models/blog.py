from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    subtitle: str
    body: str
    author: str
    published: bool


class UpdateBlog(BaseModel):
    title: str = None
    subtitle: str = None
    body: str = None
    author: str = None
    published: bool = None
