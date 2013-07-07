from mezzanine.pages.page_processors import processor_for
from mezzanine.conf import settings
from mezzanine.blog.models import BlogPost
from mezzanine_events.models import Event
import datetime

# TODO find a better home for this - it hides non-event pages from the event container
from mezzanine_events.models import EventContainer
def really_events(self):
	return self.children.published().filter(content_model='event').order_by('_order')
EventContainer.events = really_events

@processor_for("/")
def homeblocks(request, page):
	settings.use_editable()

	posts = BlogPost.objects.published(for_user=request.user).select_related()
	post = None
	try: post = posts[0]
	except: pass

	events = Event.objects.published(for_user=request.user).filter(end_time__gt=datetime.datetime.now()).order_by('start_time')
	event = None
	try: event = events[0]
	except: pass

	return {'blog_post': post, 'event': event}
