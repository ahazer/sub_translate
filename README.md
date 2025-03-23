# Altyazı Çeviri Uygulaması

Bu Python uygulaması, SRT formatındaki altyazı dosyalarını Google Translate API kullanarak otomatik olarak çevirir. İngilizce altyazıları Türkçe'ye çevirebilir ve ilerleme durumunu gerçek zamanlı olarak gösterir.

## Özellikler

- SRT formatındaki altyazı dosyalarını destekler
- Google Translate API kullanarak ücretsiz çeviri
- Gerçek zamanlı ilerleme göstergesi
- Hata yönetimi ve otomatik yeniden deneme
- Detaylı çeviri istatistikleri

## Kurulum

1. Projeyi klonlayın veya indirin
2. Gerekli Python paketlerini yükleyin:

```bash
pip install -r requirements.txt
```

## Kullanım

1. `sub_translater.py` dosyasını açın
2. `input_file` ve `output_file` değişkenlerini kendi dosya yollarınızla güncelleyin:

```python
input_file = "kaynak_altyazi.srt"  # İngilizce altyazı dosyası
output_file = "cevrilen_altyazi.srt"  # Çevrilecek Türkçe dosya
```

3. Scripti çalıştırın:

```bash
python sub_translater.py
```

## Önemli Notlar

- İnternet bağlantısı gereklidir
- Google Translate API kullanım limitlerine dikkat edilmelidir
- Büyük dosyalar için çeviri süresi uzun olabilir
- UTF-8 karakter kodlaması kullanılmaktadır

## Hata Giderme

Eğer çeviri sırasında hatalarla karşılaşırsanız:

1. İnternet bağlantınızı kontrol edin
2. Kaynak dosyanın doğru konumda olduğundan emin olun
3. Dosya kodlamasının UTF-8 olduğundan emin olun
4. Bekleme sürelerini artırmayı deneyin (`time.sleep()` değerlerini yükseltin)

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. 