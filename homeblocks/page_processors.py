from mezzanine.pages.page_processors import processor_for
from mezzanine.conf import settings
from mezzanine.blog.models import BlogPost
from mezzanine_events.models import Event

@processor_for("/")
def homeblocks(request, page):
	settings.use_editable()

	posts = BlogPost.objects.published(for_user=request.user).select_related()
	post = None
	try: post = posts[0]
	except: pass

	events = Event.objects.published(for_user=request.user)
	event = None
	try: event = events[0]
	except: pass

	return {'blog_post': post, 'event': event}
