# Rock Cannon CMS in django with multi-language 

# Language Setup Notes

See these lines roughly in this order 

    01 RockCannonCMSDjango/settings.py:47:    'django.middleware.locale.LocaleMiddleware', # NOTE 01 This lines needs to be here in the list
    02 RockCannonCMSDjango/settings.py:110:# NOTE 02 set default to english
    03 RockCannonCMSDjango/settings.py:113:# NOTE 03 add list of languages
    04 RockCannonCMSDjango/settings.py:119:# NOTE 04 set LOCALE_PATHS and create folder "locale" in the project root
    05 RockCannonCMSDjango/settings.py:126:# NOTE 05 add these three lines, all True
    06 RockCannonCMSDjango/urls.py:21:# Note 06 import i18n_patterns
    07 RockCannonCMSDjango/urls.py:32:# NOTE 07 include the app module using i18n_patterns (my main module is called cms_main)
    08 cms_main/urls.py:3:# Note 08 include this function but with an alias '_' to make the code neater
    09 cms_main/urls.py:8:# Note 09 the URLS are then translated using _("msg")
    10 cms_main/templates/layout.html:20:    <!-- Note 10 add some trans blocks with message codes -->
    11 cms_main/templates/layout.html:28:            <!-- Note 11 url functions automatically use the current language -->
    12 cms_main/templates/layout.html:38:        <!-- Note 12 add a language switcher -->
    13 RockCannonCMSDjango/urls.py:28:    # Note 13 this is needed for the language switcher
    14 README.md:7:### Note 14 to create the PO files run
    15 README.md:18:### Note 15 to compile the PO files to MO filse
    16 cms_main/templates/rc_detail.html:18:    <!-- NOTE 16 as there is only two langs, this is OK, probably a better pattern -->



### Note 14 to create the PO files run
Hist: Do this any time you add new message codes in `trans` blocks or use `_(...)`

    python manage.py makemessages -l en
    python manage.py makemessages -l en

This will regenerate files in the `locale` folder (created, see Note four)




### Note 15 to compile the PO files to MO filse
Hint: Do this any time you change the PO files above
    python manage.py compilemessages
    



