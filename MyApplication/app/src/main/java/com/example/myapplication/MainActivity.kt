package com.example.myapplication

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import com.example.myapplication.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {
    private lateinit var binding: ActivityMainBinding

   // private val myDocRef:DocumentReference=FirebaseFirestore.getInstance().document("themes/welcome")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding=ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        binding.button.setOnClickListener {Geting_data("welcome")  }
        binding.button2.setOnClickListener { Geting_data("items") }
        binding.button4.setOnClickListener { startActivity(Intent(this,MainActivity3::class.java)) }
        binding.button3.setOnClickListener {  }



    }

   private fun Geting_data(themes:String){
       val i=Intent(this,MainActivity2::class.java)
       i.putExtra(MainActivity2.THEMES,themes)
       startActivity(i)
        }
}