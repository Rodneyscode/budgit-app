from django.urls import path
from . import views

urlpatterns = [
    path('',views.profilee, name='profilee' ),
    path('transactions/',views.transactions, name='transactions' ),
    path('addingastash/',views.addastash, name='createstash' ),
    path('transfers/',views.transferfunds, name='transfers' ),
    path('settings/',views.settingspage, name='settingspage' ),
    path('editprofile/',views.editprofile, name='editprofile' ),
    path('bankinginfo/',views.bankinginfo, name='bankinginfo' ),
    path('editastash/',views.editastash, name='editastash' ),
    path('edits/',views.editstash, name='edits' ),
    path('deletestash/',views.deletestash, name='dels' ),
    path('stashone/',views.stashone, name='firststash' ),
    path('stashtwo/',views.stashtwo, name='secondstash' ),
    path('stashthree/',views.stashthree, name='thirdstash' ),
    path('stashfour/',views.stashfour, name='fourthstash' ),
    path('stashfive/',views.stashfive, name='fifthstash' ),
]