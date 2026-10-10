# Escape From The Chef: site + Android APK

Ücretsiz, reklamsız yayın. Hem oyun sitesi hem indirilebilir Android APK otomatik yapılır.

## Bir kez yapılacaklar
1. github.com'da hesap aç (siteye kayıt olurken yaş kuralını kontrol et).
2. **New repository** > adı örneğin `escape-from-the-chef` > **Public** seç (ücretsiz site için public gerekir).
3. Bu klasörün içindekileri, **`.github` klasörü dahil**, repoya yükle (Add file > Upload files).
4. Repo > **Settings > Pages > Source: GitHub Actions** seç.
5. Repo > **Actions** sekmesinde iki akış çalışır: **Deploy site** ve **Build Android APK**. Yeşil olunca bitti (APK birkaç dakika sürer).

## Sonuç
- Site: `https://KULLANICIADIN.github.io/escape-from-the-chef/`
- Oyun: sitedeki **Tarayıcıda oyna** düğmesi (`/play/`). Telefonda Chrome menüsünden "Ana ekrana ekle" ile uygulama gibi kurulur.
- APK: sitedeki **Android APK** düğmesi. Dosya repodaki **Releases** bölümüne otomatik eklenir.

## Oyunu güncellemek
`www/index.html` dosyasını yenisiyle değiştirip yükle. Site ve APK yeniden yapılır.

## APK kurulumu
APK'ya telefonda dokun, "bilinmeyen kaynaklardan yükleme" iznini ver, kur. Bu debug APK'dır, arkadaşlarla paylaşmak için uygundur; Play Store için imzalı sürüm gerekir (`docs/PLAY_LATER.md`).


## İndirme sitesi (site/ klasörü)

`site/` = oyunun indirme sayfası (TR/EN). İki yayın yolu:

**A) GitHub Pages (önerilen, bu repo ile otomatik):** repoyu GitHub'a yükle → Settings > Pages > Source: GitHub Actions. `pages.yml` siteyi `https://KULLANICI.github.io/REPO/` adresine, oyunu `/play/` altına koyar. APK'yı `build-apk.yml` Release olarak yayınlar; indir düğmesi `releases/latest/download/escape-from-the-chef.apk` adresini otomatik bulur.

**B) Netlify / Cloudflare Pages (sürükle-bırak):** `indirme-sitesi.zip` içindeki klasörü yükle. APK'yı `downloads/escape-from-the-chef.apk` olarak koy (dosya yoksa düğme "Çok yakında" der). Başka bir APK adresi için `config.js` içindeki `apk` alanını doldur.

Paylaşım önizlemesi için `index.html` içindeki `og:image` değerini tam adresle (https://siten.com/og.jpg) değiştir.
