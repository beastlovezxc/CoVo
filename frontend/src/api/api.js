/*
 * @Author: BeanCB
 * @Date: 2020-05-24 15:32:37
 * @LastEditors: BeanCB
 * @LastEditTime: 2020-05-24 15:34:06
 * @Description: file content
 * @FilePath: /Covo/frontend/src/api/api.js
 */ 

import axiosInstance from './index'

const axios = axiosInstance

export const loginCheck = () => {return axios.get(`http://localhost:8000/Users/login/`)}

export const postBook = (bookName, bookAuthor) => {return axios.post(`http://localhost:8000/api/books/`, {'name': bookName, 'author': bookAuthor})}
