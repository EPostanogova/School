package com.example.test


import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.EditText
import androidx.fragment.app.DialogFragment
import androidx.fragment.app.activityViewModels
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase


class DialogFragment : DialogFragment() {

    lateinit var mInput: EditText
    private lateinit var mActionOk: Button
    private lateinit var mActionCancel: Button
    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        val view: View = inflater.inflate(
            R.layout.dialog, container, false
        )
        mActionCancel = view.findViewById(R.id.no)
        mActionOk = view.findViewById(R.id.yes)
        mInput = view.findViewById(R.id.editTextTextPersonName)
        mActionCancel.setOnClickListener { dialog?.dismiss() }
        mActionOk.setOnClickListener {
                val input = mInput.text.toString()
            onItemClicked(input)
            val database = Firebase.database
            val myRef=database.getReference(input)
            myRef.setValue("тут")

            dialog?.dismiss()
            }
        return view
    }

    private val viewModel: ItemViewModel by activityViewModels()

    // Called when the item is clicked
    fun onItemClicked(item: String) {

        viewModel.selectItem(item)
    }




}