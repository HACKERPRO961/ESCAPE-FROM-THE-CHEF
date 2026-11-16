#!/usr/bin/env python3
"""cap add android sonrası çalışır: manifest, sürüm, imza, reklam kimlikleri.
Ortam değişkenleri (hepsi isteğe bağlı):
  VERSION_CODE, VERSION_NAME, ADMOB_APP_ID, ADMOB_REWARDED_ID, ADMOB_INTERSTITIAL_ID, SIGN=1
"""
import os, re, sys
man = 'android/app/src/main/AndroidManifest.xml'
gr = 'android/app/build.gradle'
www = 'www/index.html'

m = open(man, encoding='utf-8').read()
if 'screenOrientation' not in m:
    m = m.replace('<activity', '<activity android:screenOrientation="portrait"', 1)
m = re.sub(r'android:allowBackup="[^"]*"', 'android:allowBackup="false"', m)
app_id = os.environ.get('ADMOB_APP_ID') or 'ca-app-pub-3940256099942544~3347511713'  # Google test kimliği
if 'com.google.android.gms.ads.APPLICATION_ID' not in m:
    m = m.replace('</application>', '<meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="%s"/></application>' % app_id)
open(man, 'w', encoding='utf-8').write(m)

g = open(gr, encoding='utf-8').read()
g = re.sub(r'versionCode \d+', 'versionCode %s' % os.environ.get('VERSION_CODE', '1'), g, count=1)
g = re.sub(r'versionName "[^"]*"', 'versionName "%s"' % os.environ.get('VERSION_NAME', '1.4.0'), g, count=1)
if os.environ.get('SIGN') == '1' and 'signingConfigs' not in g:
    sign = '''    signingConfigs {
        release {
            storeFile file(System.getenv("KS_PATH"))
            storePassword System.getenv("KS_PASS")
            keyAlias System.getenv("KEY_ALIAS")
            keyPassword System.getenv("KEY_PASS")
        }
    }
    buildTypes {'''
    g = g.replace('    buildTypes {', sign, 1)
    g = g.replace('        release {\n            minifyEnabled false', '        release {\n            signingConfig signingConfigs.release\n            minifyEnabled false', 1)
open(gr, 'w', encoding='utf-8').write(g)

# Gerçek reklam kimlikleri verildiyse oyuna işle (test modu kapanır)
h = open(www, encoding='utf-8').read()
rid, iid = os.environ.get('ADMOB_REWARDED_ID'), os.environ.get('ADMOB_INTERSTITIAL_ID')
if rid and iid:
    h = h.replace('ca-app-pub-3940256099942544/5224354917', rid).replace('ca-app-pub-3940256099942544/1033173712', iid).replace('test:true', 'test:false')
    print('Gerçek AdMob kimlikleri kullanılıyor')
else:
    print('UYARI: AdMob TEST kimlikleri kullanılıyor (gelir getirmez)')
# Faturalandırma paketi (CI'da üretilir) oyundan önce yüklensin
if 'iap.bundle.js' not in h:
    h = h.replace('</head>', '<script src="iap.bundle.js"></script></head>', 1)
open(www, 'w', encoding='utf-8').write(h)
print('android-setup tamam')
