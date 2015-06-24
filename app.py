import tornado.ioloop
import tornado.web
from temboo.Library.Tumblr.Post import RetrievePublishedPosts
from temboo.core.session import TembooSession
from tornado.escape import json_decode, json_encode

session = TembooSession("jordanemedlock", "PsychTruths", "SFiEEZ8RCnzX8U8nSAbsM0QII3gcEZl6")
choreo = RetrievePublishedPosts(session)

def readJSON(fileName):
  f = open(fileName)
  return json_decode(f.read())

def writeJSON(fileName, json):
  f = open(fileName, 'w')
  f.write(json_encode(json))

def getTags(update=True):
  if update:
    posts, num_posts = getPosts(0)
    high = num_posts/10+1
    print high
    for page in xrange(1,high):
      posts2, _ = getPosts(page)
      posts += posts2
    tags = dict()
    for post in posts:
      for tag in post['tags']:
        if tag in tags:
          tags[tag] += 1
        else:
          tags[tag] = 1
    return posts, tags
  else:
    return readJSON('tags.json')

def matches(query):
  def inner(post):
    def exists(name, d):
      return name in d and d[name] is not None
    tagMatches = query in post['tags']
    titleMatches = exists('title',post) and query.lower() in post['title'].lower()
    bodyMatches = exists('body', post) and query.lower() in post['body'].lower()
    return tagMatches or titleMatches or bodyMatches
  return inner

def getPosts(page, update=True, tag=None, query=None):
  if update:
    choreo_inputs = choreo.new_input_set()

    choreo_inputs.set_APIKey("u06kxugAWrGDtTxfU5IikKXg8oXyfFO8JqabS5HDyq3qPYquHH")
    choreo_inputs.set_BaseHostname("psychologyfacts.tumblr.com")
    choreo_inputs.set_Limit("10")
    choreo_inputs.set_Offset(str(page * 10))

    results = choreo.execute_with_results(choreo_inputs)

    results = json_decode(results.get_Response())

    return results['response']['posts'], results['response']['total_posts']
  else:
    posts = readJSON("posts.json")
    if tag is not None:
      posts = filter(lambda x: tag in x['tags'], posts)
    if query is not None:
      posts = filter(matches(query), posts)
    return posts, len(posts)

class BlogHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(self, page):
    base_url="/%s"

    page = int(page or 0)

    blog_posts, num_posts = getPosts(page, update=False)
    blog_posts = blog_posts[page*10:(page+1)*10]
    has_next = (page+1)*10 <= num_posts
    has_prev = page > 0
    tags = getTags(update=False)
    tags = sorted(tags.iteritems(), cmp=lambda x,y:cmp(x[1],y[1]), reverse=True)
    self.render("blog.html", 
      blog_posts=blog_posts, 
      has_prev=has_prev, 
      has_next=has_next, 
      page=page, 
      tags=tags,
      this_tag=None,
      query=None,
      base_url=base_url)

class TagHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(self, tag, page):
    base_url = "/tag/"+tag+"/%s"

    page = int(page or 0)

    blog_posts, num_posts = getPosts(page, update=False, tag=tag)
    blog_posts = blog_posts[page*10:(page+1)*10]
    has_next = (page+1)*10 <= num_posts
    has_prev = page > 0
    tags = getTags(update=False)
    tags = sorted(tags.iteritems(), cmp=lambda x,y:cmp(x[1],y[1]), reverse=True)
    self.render("blog.html", 
      blog_posts=blog_posts, 
      has_prev=has_prev, 
      has_next=has_next, 
      page=page, 
      tags=tags,
      this_tag=tag,
      query=None,
      base_url=base_url)


class SearchHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(self, page):
    base_url = "/search/%s"

    query=self.get_argument('query',default='')

    page = int(page or 0)

    blog_posts, num_posts = getPosts(page, update=False, query=query)
    blog_posts = blog_posts[page*10:(page+1)*10]
    has_next = (page+1)*10 <= num_posts
    has_prev = page > 0
    tags = getTags(update=False)
    tags = sorted(tags.iteritems(), cmp=lambda x,y:cmp(x[1],y[1]), reverse=True)
    self.render("blog.html", 
      blog_posts=blog_posts, 
      has_prev=has_prev, 
      has_next=has_next, 
      page=page, 
      tags=tags,
      this_tag=None,
      query=query,
      num_posts=num_posts,
      base_url=base_url)


class UpdateHandler(tornado.web.RequestHandler):
  @tornado.web.asynchronous
  def get(self):
    posts, tags = getTags()
    writeJSON("posts.json", posts)
    writeJSON("tags.json", tags)
    print "all done"
    self.redirect('/')


settings = {
  "template_path": "templates",
  "autoreload": True
}

application = tornado.web.Application([
  (r"/update/?", UpdateHandler),
  (r"/([0-9]*)", BlogHandler),
  (r"/tag/([^/]*)/?([0-9]*)", TagHandler),
  (r"/search/?([0-9]*)", SearchHandler),
  (r"/static/(.*)", tornado.web.StaticFileHandler, {"path":"static"})
], **settings)


if __name__ == "__main__":
  application.listen(3000)
  tornado.ioloop.IOLoop.current().start()