import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
	routes: [{
			path: '/Home',
			name: 'Index',
			component: resolve => require(['../pages/index.vue'], resolve)
		},
		{
			path: '/index',
			name: 'Index',
			redirect: '/Home'
		},
		{
			path: '/',
			name: 'ho',
			redirect: '/Home'
		},
		{
			path: '/Blog',
			name: 'blog',
			component: resolve => require(['../pages/Blog.vue'], resolve)
		},
		{
			path: '/Music',
			name: 'music',
			component: resolve => require(['../pages/Music.vue'], resolve)
		},
		{
			path: '/Me',
			name: 'me',
			component: resolve => require(['../pages/Me.vue'], resolve)
		},
		{
			path: '/Cartoon',
			name: 'cartoons',
			component: resolve => require(['../pages/Cartoon.vue'], resolve)
		},
		{
			path: '/Passage/:id',
			name: 'passage',
			component: resolve => require(['../pages/Passage.vue'], resolve)
		},
		{
			path: '/cartoon/:id',
			name: 'cartoon',
			component: resolve => require(['../pages/Cartoon_1.vue'], resolve)
		},
		{
			path: '/404',
			name: '404',
			component: resolve => require(['../pages/404.vue'], resolve)
		},
		{
			path: '*',
			redirect: '/404'
		},
	]
})
