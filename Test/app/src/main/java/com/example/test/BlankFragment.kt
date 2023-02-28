package com.example.test

import android.graphics.BitmapFactory
import android.os.Bundle
import android.util.Log
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.fragment.app.Fragment
import com.google.android.gms.tasks.OnFailureListener
import com.google.android.gms.tasks.OnSuccessListener
import com.google.firebase.storage.FileDownloadTask
import com.google.firebase.storage.FirebaseStorage
import java.io.File
import java.io.IOException


class BlankFragment : Fragment() {

    var storage = FirebaseStorage.getInstance()

    lateinit var img:ImageView
    lateinit var text:TextView
    var myDataFromActivity: String?=null


    override fun onCreateView(
        inflater: LayoutInflater, container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {

        val view=inflater.inflate(R.layout.fragment_blank, container, false)
        img=view.findViewById(R.id.imageView)
        text=view.findViewById(R.id.textView)
        val activity: MainActivity2? = activity as MainActivity2?
        myDataFromActivity = activity?.getMyData()
        Log.d("myLog","$myDataFromActivity")
        text.text=myDataFromActivity.toString()

        return view
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
        val storageRef = storage.getReferenceFromUrl("gs://foto-21f47.appspot.com").child("$myDataFromActivity.jpg")


        try {
            val localFile: File = File.createTempFile("images", "jpg")
            storageRef.getFile(localFile)
                .addOnSuccessListener(OnSuccessListener<FileDownloadTask.TaskSnapshot?> {
                    val bitmap = BitmapFactory.decodeFile(localFile.getAbsolutePath())
                    img.setImageBitmap(bitmap)
                }).addOnFailureListener(OnFailureListener { })
        } catch (e: IOException) {
        }
    }

}