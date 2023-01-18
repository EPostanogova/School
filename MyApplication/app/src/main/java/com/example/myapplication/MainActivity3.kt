package com.example.myapplication

import android.os.Bundle
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMain3Binding
import com.google.firebase.firestore.DocumentReference
import com.google.firebase.firestore.FirebaseFirestore

class MainActivity3 : AppCompatActivity() {
    private lateinit var binding: ActivityMain3Binding

    private val myDocRef: DocumentReference = FirebaseFirestore.getInstance().document("personal_data/progress")
    var level:String="0"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMain3Binding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.button5.setOnClickListener { write_bd("level") }
    }
    private fun write_bd(collection:String){
        myDocRef?.get()?.addOnSuccessListener{ result ->
            if(result.exists()) run {
                val current_level: String? = result.getString(collection)
                level=current_level.toString()
            }
        }
            ?.addOnFailureListener { exception ->
                Log.w("firebase", "Error getting documents.", exception)
            }

        var next=Integer.parseInt(level)
        next++
        level=next.toString()

        val dataSave:HashMap<String,String> = HashMap<String,String>()
        dataSave.put("level",level)

        myDocRef.set(dataSave).addOnCompleteListener { task->
            if(task.isSuccessful()){
                Log.d("firebase", "Successful.")
            }
            else  Log.d("firebase", "Error. ${task.exception}")
        }

        binding.textView2.text=level
    }
}