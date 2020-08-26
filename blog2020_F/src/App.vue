<template>
	<div id="app">
		<router-view ></router-view>
	</div>
</template>

<script>
	import {webRead} from './api/api.js'
	export default {
		name: 'App',
		mounted() {
			if (this.$store.state.webReadPerson == 0){
				webRead().then(res=>{
					const record = res.data.websiteReadPerson
					this.$store.dispatch('savewebReadPerson',record)
				})
			}
		}
	}
</script>

<style>
	@import url("./assets/scss/basic.scss");
	@import url("./assets/scss/reset.scss");
	@import url("./assets/scss/mixin.scss");
	#app {
		font-family: 'Avenir', Helvetica, Arial, sans-serif;
	}
</style>
