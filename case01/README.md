# Food-101 Görüntü Sınıflandırma Projesi — Full Report

---

## Proje Genel Tanıtımı

Bu çalışmada, popüler Food-101 görüntü sınıflandırma veri seti kullanılarak, derin öğrenme tabanlı farklı modellerle yiyecek kategorilerinin sınıflandırılması hedeflenmiştir.

Çalışma iki farklı projeden oluşmaktadır:

- **5Katagori_Resnet18:** Food-101 veri setinden seçilen **5 kategori** (pizza, hamburger, sushi, french fries, ice cream) üzerinde ResNet-18 modeli ile transfer öğrenme yöntemi
 kullanılarak sınıflandırma yapılmıştır.
- **Proje 2:** Food-101 veri setinden seçilen **20 kategori** üzerinde VGG16 ve ResNet18 modelleri ile transfer öğrenme, freez ve ince ayar (fine-tuning) yöntemleri uygulanmıştır. 
İnce ayar ve hiperparametre düzenlemeleriyle model performansı artırılmıştır.

---

## 5Katagori_Resnet18: 5 Kategori Üzerinde ResNet-18 ile Sınıflandırma

### Kullanılan Kategoriler
- pizza  
- hamburger  
- sushi  
- french_fries  
- ice_cream  

### Veri Seti ve Ön İşleme
- Her kategori için 750 eğitim ve 250 test görüntüsü seçildi.
- Görüntüler 224x224 boyutuna yeniden boyutlandırıldı.
- Veri artırma (data augmentation) teknikleri uygulandı: yatay çevirme, rastgele döndürme, zoom, kaydırma.
- Piksel değerleri normalize edildi.
- Veri %75 eğitim, %10 doğrulama, %15 test olarak bölündü.

### Model Seçimi ve Eğitimi
- **Model:** ResNet-18  
- **Neden ResNet-18?**  
  Residual bağlantıları sayesinde derin ağlarda gradyan kaybını önler, ImageNet önceden eğitilmiş ağırlıkları transfer öğrenmede avantaj sağlar.
- **Transfer Öğrenme:**  
  Önceden eğitilmiş ImageNet ağırlıkları kullanıldı ve son katmanlar 5 kategori için yeniden eğitildi.
- **Erken Durdurma (Early Stopping):**  
  Modelin doğrulama performansı (özellikle F1 skoru) belirli sayıda epoch boyunca iyileşmediğinde (bu projede 3 epoch) eğitim durdurulur. 
  Bu, aşırı öğrenmenin (overfitting) önüne geçmek ve gereksiz zaman kaybını engellemek için uygulanır.   
  Eğitim, 30 epoch yerine doğrulama skorlarındaki 3 kere iyileşme durduğunda eğitim duryor 
  **10 epoch'ta iyileşebilir olmasına rağmen erken durduruldu**. Böylece zaman kaybı önlendi ve en iyi model ağırlıkları saklandı.

### Eğitim Sonuçları (10. Epoch)
| Metrik               | Değer    |
|----------------------|----------|
| Train Loss           | 0.5447   |
| Train Accuracy       | 80.85%   |
| Validation Loss      | 0.2765   |
| Validation Accuracy  | 90.60%   |
| Validation Precision | 0.9071   |
| Validation Recall    | 0.9060   |
| Validation F1 Score  | 0.9059   |

- En iyi model `best_model_resnet.pth` olarak kaydedildi.

### Model Değerlendirme
- Test setinde accuracy, precision, recall ve F1 skorları hesaplandı.
- Confusion matrix görselleştirildi.

### Zorluklar
- Veri setinin tamamı çok büyük olduğu için sadece 5 kategori seçildi.

### İyileştirme Önerileri
- Daha fazla kategori ile çalışma.
- Öğrenme oranı zamanlaması ve erken durdurma.
- Farklı mimari ve ensemble modeller.
- Hiperparametre optimizasyonu.

---

## Proje 2: 20 Kategori Üzerinde VGG16 ve ResNet18 Transfer Öğrenme ve İnce Ayar

### Genel Bakış
- 20 farklı Food-101 kategorisi seçildi.
- CNN mimarileri VGG16 ve ResNet18 kullanıldı.
- Transfer öğrenme ve ince ayar teknikleri ile performans artırıldı.
- Ek katmanlar ve dropout oranları ile model iyileştirildi.
- İnce ayar yapılırken bazı modellerde feature extraction (katman kilitleme) yapıldı, bazılarında tüm katmanlar serbest bırakıldı.
- Erken durdurma ve öğrenme oranı ayarlaması uygulandı.

### Önemli Deney Sonuçları
| Model ve Değişiklik                                  | Doğrulama/Test Doğruluğu (%) |
|-----------------------------------------------------|------------------------------|
| ResNet (tüm katmanlar ince ayar)                    | 71.98                        |
| ResNet (tüm katmanlar ince ayar, yüksek öğrenme hızı)| 44.21                        |
| ResNet (sadece fully connected katman ince ayar)   | 66.78                        |
| ResNet (1 veya 2 rezidüel blok kaldırıldı)          | 51.6 - 53.12 arası            |
| VGG (tüm katmanlar ince ayar, uygun öğrenme hızı)  | 74.40                        |
| VGG (feature extraction, katman kilitli)            | 68.62                        |

### Öne Çıkan Noktalar
- İnce ayar (fine-tuning) tüm katmanlarda yapılınca doğruluk önemli ölçüde arttı.
- Uygun öğrenme hızı ve erken durdurma başarıyı etkiledi.
- Ağırlık haritaları ve özellik aktivasyonları analiz edilerek model yorumlanabilirliği artırıldı.

### Kullanılan Dosyalar
- `data.py`, `prepare_data`: Veri ön işleme ve yükleme.
- `model.py`: Model mimarileri ve yapılandırmaları.
- Jupyter Notebook dosyaları:
  - `resnet18_InceAyar.ipynb`
  - `resnet_kilitli.ipynb`
  - `vgg_InceAyar.ipynb`
  - `vgg_Kilitli.ipynb`

---

## Genel Sonuç ve Öneriler

- 5Katagori_Resnet18’de sınırlı kategoriyle hızlı ve başarılı bir model geliştirildi.  
- Proje 2’de daha geniş kategori seti ve detaylı ince ayar ile model performansı yükseltildi.  
- Transfer öğrenme ve ince ayar derin öğrenme projelerinde çok önemli ve etkili tekniklerdir.  
- İleri aşamada, farklı modellerin karşılaştırılması, hiperparametre optimizasyonu, ensemble yaklaşımları ve veri artırma tekniklerinin detaylandırılması önerilir.

---

## Çalıştırma Talimatları

- Proje kodları Jupyter Notebook formatındadır.
- Gerekli Python kütüphaneleri `requirements.txt` içinde listelenmiştir.
- Modeller `.pth` dosyaları olarak kaydedilmiştir.
- Google Colab veya lokal ortamda kolayca çalıştırılabilir.

---

## Ek Notlar

- Proje 1’de erken durdurma ile 30 epoch yerine 10 epoch’ta eğitim tamamlandı. Bu, zaman kazanmak ve overfitting’i engellemek için stratejik bir yaklaşımdır.

---
