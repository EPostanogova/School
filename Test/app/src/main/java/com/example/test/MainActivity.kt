package com.example.test


import android.graphics.drawable.BitmapDrawable
import android.os.Bundle
import android.util.Log
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.Observer
import androidx.recyclerview.widget.LinearLayoutManager
import com.example.test.databinding.ActivityMainBinding
import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.ktx.auth
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.DatabaseReference
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase
import com.squareup.picasso.Picasso


class MainActivity : AppCompatActivity() {
    lateinit var binding: ActivityMainBinding
    lateinit var auth: FirebaseAuth
    lateinit var adapter: Adapter
    var myDataFromActivity: String?=null
    private val viewModel: ItemViewModel by viewModels()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)
        auth = Firebase.auth
//        setUpActionBar()
        val database = Firebase.database
        viewModel.selectedItem.observe(this, Observer { item ->
            myDataFromActivity= item.toString()
        })



     //   onChangeListener(myRef)
        initRcView()
        binding.button.setOnClickListener {
           showNoticeDialog()
            val myRef = database.getReference("messages")
            myRef.setValue("Hello, World!")
        }




    }

    private fun initRcView() = with(binding){
        adapter = Adapter()
        rv.layoutManager = LinearLayoutManager(this@MainActivity)
        val data = ArrayList<Chat_List>()

        for (i in 1..10) {
            data.add(Chat_List(myDataFromActivity.toString()))
        }
        rv.adapter = adapter
    }
//
//
//    private fun onChangeListener(dRef: DatabaseReference){
//        dRef.addValueEventListener(object : ValueEventListener {
//            override fun onDataChange(snapshot: DataSnapshot) {
//                val list = ArrayList<Chat_List>()
////                for(s in snapshot.children){
////                    val user = s.getValue(Chat_List::class.java)
////                    if(user != null)list.add(user)
////                }
////                adapter.submitList(list)
//            }
//
//            override fun onCancelled(error: DatabaseError) {
//
//            }
//
//        })
//    }
//
//    private fun setUpActionBar(){
//        val ab = supportActionBar
//        Thread{
//            val bMap = Picasso.get().load(auth.currentUser?.photoUrl).get()
//            val dIcon = BitmapDrawable(resources, bMap)
//            runOnUiThread {
//                ab?.setDisplayHomeAsUpEnabled(true)
//                ab?.setHomeAsUpIndicator(dIcon)
//                ab?.title = auth.currentUser?.displayName
//            }
//        }.start()
//
//    }
    fun showNoticeDialog() {
        // Create an instance of the dialog fragment and show it
        val dialog = DialogFragment()
        dialog.show(supportFragmentManager, "NoticeDialogFragment")
    }
}