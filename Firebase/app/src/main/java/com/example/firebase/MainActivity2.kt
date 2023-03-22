package com.example.firebase

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.activity.viewModels
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.example.firebase.databinding.ActivityMain2Binding

class MainActivity2 : AppCompatActivity() {
    lateinit var b:ActivityMain2Binding
    var nameChat: String? =null

    private val dataModel:DataModel by viewModels()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        b=ActivityMain2Binding.inflate(layoutInflater)
        setContentView(b.root)
        b.rv.layoutManager = LinearLayoutManager(this)



        b.button.setOnClickListener {  showNoticeDialog()
            dataModel.name.observe(this,{
                nameChat=it })

        }
        val data = ArrayList<ItemsViewModel>()
        val adapter = Adapter2(data)
        b.button3.setOnClickListener {
            data.add(ItemsViewModel(nameChat.toString(),R.drawable.img_1))
            b.rv.adapter=adapter
        }


    }


    fun showNoticeDialog() {
        // Create an instance of the dialog fragment and show it
        val dialog =DialogFragment()
        dialog.show(supportFragmentManager, "NoticeDialogFragment")
    }

}