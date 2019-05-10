from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.core.paginator import Paginator
from yuedu.models import ReadType,Article,ReadTag

# Create your views here.



class YueduView(View):

    read_types = ReadType.objects.all().order_by('index')

    news_articles = Article.objects.all().order_by('-create_time')[:8]

    hot_articles = Article.objects.all().order_by('-readcount')[:8]

    hot_tags = ReadTag.objects.all().order_by('-create_time')[:15]




class IndexView(YueduView):
    def get(self,request):

        arts = Article.objects.all().order_by('-create_time')[:20]



        context = {'read_types': YueduView.read_types,
                    'new_articles': YueduView.news_articles,
                    'hot_articles': YueduView.hot_articles,
                    'hot_tags': YueduView.hot_tags,
                    'arts':arts,

                    }

        return render(request,'index.html',context)




class ListView(YueduView):
    def get(self,request,type_id,page):
        try:
            type = ReadType.objects.get(id=type_id)
        except ReadType.DoesNotExsit:
            return redirect(reverse('index:index'))

        types = ReadType.objects.all()

        articles = Article.objects.filter(read_type=type).order_by('-id')

        paginator = Paginator(articles,1)

        try:
            page = int(page)
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1


        articles_page = paginator.page(page)

        num_pages = paginator.num_pages

        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        context = {
            'read_types': YueduView.read_types,
            'new_articles': YueduView.news_articles,
            'hot_articles': YueduView.hot_articles,
            'hot_tags': YueduView.hot_tags,
            'articles_page':articles_page,
            'type':type,
        }

        return render(request,'list.html',context)



class DetailView(YueduView):
    def get(self,request,art_id):


        try:
            article = Article.objects.get(id=art_id)
        except Article.DoseNotExsit:
            return redirect(reverse('index:index'))


        # try:
        #     previous_art = Article.objects.all(id=art_id).first()
        # except Exception as e:
        #     pass
        #
        #
        #
        # try:
        #     next_art = Article.objects.all(id=art_id).last()
        # except Exception as e:
        #     pass

        same_articles = Article.objects.filter(read_type=article.read_type).exclude(id=art_id).order_by('-create_time')[:10]

        article.readcount += 1
        article.save()

        context = {'read_types': YueduView.read_types,
                   'new_articles': YueduView.news_articles,
                   'hot_articles': YueduView.hot_articles,
                   'hot_tags': YueduView.hot_tags,
                   'article':article,
                   'same_articles':same_articles

                   }

        return render(request,'detail.html',context)



class TagsView(YueduView):
    def get(self,request,tag,page):

        try:
            tags = ReadTag.objects.get(read_tag=tag)
        except ReadTag.DoesNotExsit:

            return redirect(reverse('index:index'))

        # types = ReadType.objects.all()

        articles = Article.objects.filter(read_tag_info=tags).order_by('-id')

        paginator = Paginator(articles, 1)

        try:
            page = int(page)
        except Exception as e:
            page = 1
        if page > paginator.num_pages:
            page = 1

        articles_page = paginator.page(page)

        num_pages = paginator.num_pages

        if num_pages < 5:
            pages = range(1, num_pages + 1)
        elif page <= 3:
            pages = range(1, 6)
        elif num_pages - page <= 2:
            pages = range(num_pages - 4, num_pages + 1)
        else:
            pages = range(page - 2, page + 3)

        context = {
            'read_types': YueduView.read_types,
            'new_articles': YueduView.news_articles,
            'hot_articles': YueduView.hot_articles,
            'hot_tags': YueduView.hot_tags,
            'articles_page': articles_page,
            'tags':tags
        }

        return render(request, 'list2.html', context)
