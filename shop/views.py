from django.http import HttpResponse

# 1. Страница об авторе
def about(request):
    return HttpResponse("Автор лабораторной работы: Тригорлова Анастасия, 88ТП.")

# 2. Страница о магазине
def store_info(request):
    text = "Тема лабораторной работы: Магазин товаров для ухода за комнатными растениями."
    return HttpResponse(text)

# 3. Главная страница с ссылками
def home(request):
    html = """
    <h1>Главная страница магазина</h1>
    <ul>
        <li><a href='/about/'>Об авторе</a></li>
        <li><a href='/info/'>О магазине</a></li>
    </ul>
    """
    return HttpResponse(html)
# Create your views here.
