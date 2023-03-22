package com.example.firebase

import androidx.lifecycle.MutableLiveData
import androidx.lifecycle.ViewModel

class DataModel:ViewModel() {
    val name:MutableLiveData<String> by lazy {
        MutableLiveData<String>()
    }

}