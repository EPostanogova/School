package com.example.test

import android.view.LayoutInflater
import android.view.ViewGroup

import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.example.test.databinding.CardBinding



class Adapter : ListAdapter<Chat_List, Adapter.ItemHolder>(ItemComparator()) {

    class ItemHolder(private val binding: CardBinding) : RecyclerView.ViewHolder(binding.root){
        fun bind(user: Chat_List) = with(binding){
            chat.text = user.name_chat

        }
        companion object{
            fun create(parent: ViewGroup): ItemHolder{
                return ItemHolder(CardBinding
                    .inflate(LayoutInflater.from(parent.context), parent, false))
            }
        }
    }

    class ItemComparator : DiffUtil.ItemCallback<Chat_List>(){
        override fun areItemsTheSame(oldItem: Chat_List, newItem: Chat_List): Boolean {
            return oldItem == newItem
        }

        override fun areContentsTheSame(oldItem: Chat_List, newItem:Chat_List): Boolean {
            return oldItem == newItem
        }

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ItemHolder {
        return ItemHolder.create(parent)
    }

    override fun onBindViewHolder(holder: ItemHolder, position: Int) {
        holder.bind(getItem(position))
    }
}