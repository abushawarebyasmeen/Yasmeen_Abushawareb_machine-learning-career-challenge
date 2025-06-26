
"""prepare_data.ipynb
"""

import csv
import json

# Veri setini yükler ve işler
def get_data():
    train_data_dict, test_data_dict = {}, {}
    train_data, test_data = [], []

    # Sınıfları oku ve her 5. sınıfı seç (20 tane)
    with open('food-101/meta/classes.txt', 'r') as f:
        classes = f.readlines()
        classes = [_class.rstrip('\n') for _class in classes]
        classes_to_use_indices = [i for i in range(1, 101, 5)]
        classes_to_use = [classes[i] for i in classes_to_use_indices]

    # Etiketleri oku ve aynı şekilde seç
    with open('food-101/meta/labels.txt', 'r') as f:
        labels = f.readlines()
        labels = [_class.rstrip('\n') for _class in labels]
        labels_to_use_indices = [i for i in range(1, 101, 5)]
        labels_to_use = [labels[i] for i in labels_to_use_indices]

        # Sınıf-adı → etiket ve etiket → index sözlükleri oluştur
        class2label = dict(zip(classes_to_use, labels_to_use))
        indices = list(range(0, 20))
        label2idx = dict(zip(labels_to_use, indices))

    # Eğitim verisini yükle
    with open('food-101/meta/train.json', 'r') as f:
        train_data_raw = json.load(f)
        for _class in classes_to_use:
            train_data_dict[class2label[_class]] = train_data_raw[_class]

    # Test verisini yükle
    with open('food-101/meta/test.json', 'r') as f:
        test_data_raw = json.load(f)
        for _class in classes_to_use:
            test_data_dict[class2label[_class]] = test_data_raw[_class]

    # Eğitim verisi: [resim_yolu, etiket, index]
    for label in train_data_dict:
        _data_in_class = train_data_dict[label]
        idx = label2idx[label]
        for relative_path in _data_in_class:
            fp = 'food-101/images/{}.jpg'.format(relative_path)
            train_data.append([fp, label, idx])

    # Test verisi: [resim_yolu, etiket, index]
    for label in test_data_dict:
        _data_in_class = test_data_dict[label]
        idx = label2idx[label]
        for relative_path in _data_in_class:
            fp = 'food-101/images/{}.jpg'.format(relative_path)
            test_data.append([fp, label, idx])

    return train_data, test_data

# Verileri al
train_data, test_data = get_data()

# Eğitim verisini CSV'ye yaz
with open("food-101/train.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(train_data)

# Test verisini CSV'ye yaz
with open("food-101/test.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(test_data)
