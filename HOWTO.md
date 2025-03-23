# Altyazı Çeviri Uygulaması Kullanım Kılavuzu

Bu belge, altyazı çeviri uygulamasının detaylı kullanım kılavuzudur. Farklı senaryolar için adım adım talimatlar içerir.

## İçindekiler

1. [Temel Kurulum](#temel-kurulum)
2. [Basit Kullanım](#basit-kullanım)
3. [Gelişmiş Özellikler](#gelişmiş-özellikler)
4. [Sık Karşılaşılan Sorunlar](#sık-karşılaşılan-sorunlar)
5. [İpuçları ve Püf Noktaları](#ipuçları-ve-püf-noktaları)

## Temel Kurulum

### Python Kurulumu

1. [Python'un resmi sitesinden](https://www.python.org/downloads/) Python 3.7 veya üstü bir sürüm indirin
2. Kurulum sırasında "Add Python to PATH" seçeneğini işaretleyin
3. Kurulumun başarılı olduğunu kontrol etmek için terminal/komut isteminde şu komutu çalıştırın:
   ```bash
   python --version
   ```

### Uygulama Kurulumu

1. Projeyi bilgisayarınıza indirin
2. Terminal/komut isteminde proje dizinine gidin
3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Basit Kullanım

### Tek Dosya Çevirisi

1. Çevirmek istediğiniz SRT dosyasının tam yolunu not edin
2. `sub_translater.py` dosyasını bir metin editörüyle açın
3. Şu satırları kendi dosya yollarınızla güncelleyin:
   ```python
   input_file = "KAYNAK_DOSYA_YOLU.srt"
   output_file = "HEDEF_DOSYA_YOLU.srt"
   ```
4. Scripti çalıştırın:
   ```bash
   python sub_translater.py
   ```

### İlerleme Takibi

Çeviri işlemi sırasında:
- İlerleme çubuğu mevcut durumu gösterir
- Toplam satır sayısı ve işlenen satır sayısı görüntülenir
- Hatalar anlık olarak raporlanır

## Gelişmiş Özellikler

### Farklı Dil Çiftleri Kullanımı

Varsayılan olarak İngilizce'den (en) Türkçe'ye (tr) çeviri yapılır. Farklı diller için:

```python
translate_subtitles(input_file, output_file, source_lang="fr", target_lang="es")
```

Desteklenen dil kodları:
- en: İngilizce
- tr: Türkçe
- fr: Fransızca
- es: İspanyolca
- de: Almanca
(ve diğer Google Translate tarafından desteklenen diller)

### Hata Yönetimi Ayarları

Script varsayılan olarak her satır için 3 deneme yapar. Bu sayıyı değiştirmek için:

```python
max_retries = 5  # veya istediğiniz sayı
```

### Bekleme Süresi Ayarları

API limit aşımı hatalarını önlemek için bekleme sürelerini ayarlayabilirsiniz:

```python
time.sleep(1.0)  # Daha uzun bekleme süresi
```

## Sık Karşılaşılan Sorunlar

### 1. "Dosya bulunamadı" Hatası
- Dosya yolunun doğru olduğundan emin olun
- Yolda Türkçe karakter kullanmamaya çalışın
- Dosya izinlerini kontrol edin

### 2. API Hataları
- İnternet bağlantınızı kontrol edin
- Bekleme sürelerini artırın
- VPN kullanıyorsanız kapatmayı deneyin

### 3. Karakter Kodlama Hataları
- Dosyanızın UTF-8 ile kodlandığından emin olun
- Notepad++ gibi bir editör ile dosya kodlamasını kontrol edin

## İpuçları ve Püf Noktaları

1. **Performans İyileştirmeleri**
   - Büyük dosyalar için bekleme süresini artırın
   - Sistem kaynaklarını izleyin
   - Diğer uygulamaları kapatın

2. **Kalite Kontrol**
   - Çeviri bittikten sonra dosyayı manuel kontrol edin
   - Özellikle özel isimlere dikkat edin
   - Zamanlama sorunları için kontrol yapın

3. **Yedekleme**
   - İşlem öncesi kaynak dosyayı yedekleyin
   - Düzenli aralıklarla çıktı dosyasını yedekleyin

4. **Optimizasyon**
   - Çok büyük dosyaları bölerek işleyin
   - İşlem sırasında bilgisayarı meşgul etmeyin
   - RAM kullanımını izleyin

## Destek ve İletişim

Sorunlarınız veya önerileriniz için:
1. GitHub Issues bölümünü kullanın
2. Hata raporlarında log dosyalarını ekleyin
3. Problemi tekrar üretmek için gerekli adımları detaylı açıklayın 