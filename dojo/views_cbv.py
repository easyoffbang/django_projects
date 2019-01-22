from django.views.generic import View, TemplateView
from django.http import HttpResponse, JsonResponse
import os


#CBV: 직접 문자열로 html형식 응답하기
class postlistview1(View):
    def get(self, request):
        name = '공유'
        html = self.get_template_string().format(name=name)
        return HttpResponse(html)

    def get_template_string(self):
        return '''
        <h1>AskDjango</h1>
        <p>{name}</p>
        <p>여러분의 파이썬&장고 페이스메이커가 되어드리겠습니다.</p>
        '''
post_list1 = postlistview1.as_view()

#템플릿 사용
class postlistview2(TemplateView):
    template_name ='dojo/post_list.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = '공유'
        return context

post_list2 = postlistview2.as_view()


class postlistview3(View):
    def get(self, request):
        return JsonResponse(self.get_data(), json_dumps_params={'ensure_ascii': False})

    def get_data(self):
        return {
        'message': '안녕, 파이썬&장고',
        'items': ['파이썬', '장고', 'Celery', 'Azure', 'AWS'],
        }
post_list3 = postlistview3.as_view()


class exceldownloadview(View):
    excelpath = '../SearchResultList.xls'

    def get(self, request):
        filename = os.path.basename(self.excelpath)
        with open(self.excelpath, 'rb') as f:
            response = HttpResponse(f, content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
            return response

exceldownload = exceldownloadview.as_view()