package com.example.myapplication

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.myapplication.databinding.ActivityMain2Binding
import com.google.firebase.firestore.DocumentReference
import com.google.firebase.firestore.FirebaseFirestore

class MainActivity2 : AppCompatActivity() {
    private lateinit var binding: ActivityMain2Binding
    private lateinit var doc:String
    companion object{const val THEMES="name"}


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding= ActivityMain2Binding.inflate(layoutInflater)
        setContentView(binding.root)

        doc= intent.getStringExtra(THEMES).toString()

        Geting_data(doc)


    }
    private fun Geting_data(themes:String):ArrayList<ViewModel>{
        val data = ArrayList<ViewModel>()
        val myDocRef: DocumentReference = FirebaseFirestore.getInstance().document("themes/$themes")
        myDocRef?.get()?.addOnSuccessListener{ result ->
            if(result.exists()) run {
                val recyclerview = findViewById<RecyclerView>(R.id.rv)
                recyclerview.layoutManager = LinearLayoutManager(this,LinearLayoutManager.HORIZONTAL,false)
               // val data = ArrayList<ViewModel>()
                for(i in 1..3) {
                    val eng_text: String? = result.getString("eng_$i")
                    val kr_text: String? = result.getString("kr_$i")

                    data.add(ViewModel(eng_text.toString(), kr_text.toString()))
                }
                val adapter = Adapter(data)
                recyclerview.adapter = adapter


            }
        }
            ?.addOnFailureListener { exception ->
                Log.w("firebase", "Error getting documents.", exception)
            }
        return data

    }

}