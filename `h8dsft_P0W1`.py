#!/usr/bin/env python
# coding: utf-8

# # I.  Perkenalan

# Nama : Arya Bandoro
# 
# Kali ini kita akan mencoba untuk melakukan analisis data terhadap data pokemon dimana disini dari data pokemon kita dapat melakukan analisis, objective yang ingin dicapai disini adalah melihat pokemon dengan melihat dari 1 tipe yang terkuat, dengan cara membandingkan beberapa aspek diantaranya adalah, rata rata kekuatan dalam hal attack, defence dan juga speednya, sehingga dapat ditarik kesimpulan bahwa pokemon manakah berdasarkan tipe yang lebih kuat

# # II. Masukan Library Yang Dibutuhkan 

# Selanjutnya dapat kita masukan library yang dibutuhkan dimana dalam hal ini yang dibutuhkan adalah python dan juga pandas

# In[1]:


import pandas as pd #ini untuk membuat data frame
import numpy as np #untuk melakukan operasi matematika


# # III. Data Loading

# In[2]:


data1 = pd.read_csv(r'C:\Users\Acer\OneDrive\Documents\Hacktiv8\W1\Graded\Pokemon.csv') #melakukan importing data
data1 #kita coba menampilkan datanya


# In[3]:


data1.info() #melihat info datanya


# In[4]:


data1.describe().transpose() #melakukan transpose untuk dapat melihat datanya lebih luas


# # IV. Data Cleaning

# In[5]:


#disini kita tidak menggunakan kolom generation,type 2, dan legendary maka dapat kita hapus menggunakan perintah, serta untuk 
#menangani missing value juga
data_clean = data1.drop(columns=['Name','Generation', 'Legendary','Type 2','Total','#','Speed'])


# In[6]:


#sekarang kita cek lagi missing value lagi
data_clean.info()


# In[7]:


#atau dapat kita cek dengan melakukan describe
data_clean.describe().transpose()


# In[8]:


data_clean[data_clean['HP']==1] 


# In[9]:


#kita lakukan rename kolom
data_jadi = data_clean.rename(columns = {'Type 1': 'Tipe' })


# In[10]:


data_jadi


# In[11]:


data = data_jadi.sort_values("Tipe")


# In[12]:


data.tail(50)


# # V. Eksplorasi Data

# Selanjutnya kita bisa melakukan query data dimana terdapat 3 query yang akan dibuat yaitu 
# query 1 meliputi jenis dari HP nya sehingga diambil dari data statistiknya yaitu pokemon dengan HP pada kuartil 1, 2 dan 3 dimana saya akan membagi menjadi 3 kelas yaitu kelas kecil, menengah dan juga kelas berat

# In[13]:


dataHPKecil = data.query('HP < 65')
dataHPMenengah = data.query('65 <= HP < 80 ')
dataHPTinggi = data.query('HP >= 80')


# In[14]:


dataHPKecil.info()
dataHPMenengah.info()
dataHPTinggi.info()


# Lalu dari masing masing query yang sudah dibuat saya akan membuat menjadi pengelompokan data masing masing dimana dalam hal ini akan dibagi menjadi 3 kelompok yaitu kelompok kecil, menengah dan besar berdasarkan query yang kita buat tadi, dan dari soal diketahui bahwa terdapat beberapa tipe pokemon yaitu tipe water, normal, grass, bug, dan psychic

# In[15]:


#pertama kita bisa melihat masing masing datanya
dataHPKecil


# In[16]:


dataHPMenengah


# In[17]:


dataHPTinggi


# Kita dapat membuat grouping dari masing masing data yang sudah kita query tadi sehingga akan menghasilkan sebagai berikut ini

# Saya akan membagi masing masing query dengan tiga indikator, yaitu HP, Attack dan juga defence

# In[18]:


dataHPTinggi


# Dilakukan Pembersihan Data Kembali

# In[27]:


datahpfixrendah = dataHPKecil.drop(columns = ['HP','Attack','Defense','Sp. Atk','Sp. Def'])
datahpfixmenengah = dataHPMenengah.drop(columns = ['HP','Attack','Defense','Sp. Atk','Sp. Def'])
datahpfixtinggi = dataHPTinggi.drop(columns = ['HP','Attack','Defense','Sp. Atk','Sp. Def'])


# In[29]:


datahpfixrendah


# In[30]:


datahpfixmenengah


# In[31]:


datahpfixtinggi


# In[42]:


datahpfixtinggi.value_counts()


# In[43]:


datahpfixtinggi.value_counts().plot(kind='bar')


# In[44]:


datahpfixrendah.value_counts().plot(kind='bar')


# In[45]:


datahpfixmenengah.value_counts().plot(kind='bar')


# # VI. Pengambilan Kesimpulan

# Dari data visualisasi yang didapatkan berdasarkan perhitungan HP nya maka, nilai frekuensi terbesar berada pada pokemon Water untuk nilai terbanyak pada hp menengah dan juga tinggi, namun nilai dari pokemon ini terdistribusi secara sempurna terhadap seluruh HP, namun jika diperhatikan terhadap jenis pokemon dragon dimana pokemon dragon terdistribusi pada hp menengah dan tinggi, namun dari keseluruhan data nilai pokemon dragon tersebut, mayoritas berada pada nilai yang tinggi, sehingga dapat dikatakan bahwa pokemon dragon adalah salah satu yang terkuat dari keseluruhan pokemon yang ada.
