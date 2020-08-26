import axios from 'axios'
let baseUrl = 'http://47.113.81.118:8888/api'

export const Cartoons = (params) =>{
	return axios.get(`${baseUrl}/Cartoons/`,params)
}

export const Cartoon = (params) =>{
	return axios.get(`${baseUrl}/Cartoons/${params}/`)
}

export const Musics = (params) =>{
	return axios.get(`${baseUrl}/Musics/`,params)
}

export const Blogs = (params) =>{
	return axios.get(`${baseUrl}/Blogs/`,params)
}
export const Blog = (params) =>{
	return axios.get(`${baseUrl}/Blogs/${params}/`)
}

export const leaveMessages = (params) =>{
	return axios.get(`${baseUrl}/LeaveMessages/`,params)
}

export const createLeaveMessages = (data) =>{
	return axios.post(`${baseUrl}/LeaveMessages/`,data)
}


export const replyMessages = () =>{
	return axios.get(`${baseUrl}/ReplyMessages/`)
}

export const createReplyMessages = (data) =>{
	return axios.post(`${baseUrl}/ReplyMessages/`,data)
}

export const webRead = () =>{
	return axios.get(`${baseUrl}/WebReadPerson/1/`)
}