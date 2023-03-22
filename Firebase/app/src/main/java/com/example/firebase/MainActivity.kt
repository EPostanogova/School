package com.example.firebase

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import com.example.firebase.databinding.ActivityMainBinding
import com.google.firebase.database.*

class MainActivity : AppCompatActivity() {
    lateinit var binding: ActivityMainBinding
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val database = FirebaseDatabase.getInstance()
        val myRef = database.getReference("message")
        Changel(myRef)
        binding.button2.setOnClickListener {
            myRef.setValue(binding.editTextTextPersonName2.text.toString())

        }
    }
    private fun Changel(dRef: DatabaseReference) {
        dRef.addValueEventListener(object :ValueEventListener{
            override fun onDataChange(snapshot: DataSnapshot) {
                binding.apply {
                    textView2.append("\n")
                    textView2.append("Lena: ${snapshot.value.toString()}")
                }
            }
            override fun onCancelled(error: DatabaseError) {
            }   })}

}