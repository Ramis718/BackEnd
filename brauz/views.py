from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def name(request):
    return HttpResponse("Лев")

def new(request):
    return HttpResponse("Лев  — вид хищных млекопитающих, один из пяти представителей рода пантер , относящегося к подсемейству больших кошек  в составе семейства кошачьих  Наряду с тигром — самая крупная из ныне живущих кошек, масса некоторых самцов может достигать 250 кг. Трудно сказать достоверно, массивнее ли крупнейшие подвиды льва, чем крупнейшие подвиды тигров. Связано это с тем, что известные очень большие массы амурских тигров в большинстве своём признаны недостаточно достоверными. Достаточными данными о размерах и массе представителей крупнейших подвидов льва (например, барбарийском) наука не располагает. Что касается живущих в неволе животных, они часто являют собой смешение разных подвидов. Существует мнение, что львы в неволе несколько превышают тигров в размерах и массе, так же как и обратное ему.\n")

def new_1(request):
    return HttpResponse("HTTP в настоящее время повсеместно используется во Всемирной паутине для получения информации с веб-сайтов. В 2006 году в Северной Америке доля HTTP-трафика превысила долю P2P-сетей и составила 46 %, из которых почти половина — это передача потокового видео и звука. HTTP используется также в качестве «транспорта» для других протоколов прикладного уровня, таких как SOAP, XML-RPC, WebDAV.Основным объектом манипуляции в HTTP является ресурс, на который указывает URI  в запросе клиента. Обычно такими ресурсами являются хранящиеся на сервере файлы, но ими могут быть логические объекты или что-то абстрактное. Особенностью протокола HTTP является возможность указать в запросе и ответе способ представления одного и того же ресурса по различным параметрам: формату, кодировке, языку и т. д. (в частности, для этого используется HTTP-заголовок). Именно благодаря возможности указания способа кодирования сообщения клиент и сервер могут обмениваться двоичными данными, хотя данный протокол является текстовым.")