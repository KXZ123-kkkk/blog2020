<template>
	<div class="footer">
		<div class="visit">
			访问人数：{{this.$store.state.webReadPerson}}
		</div>
		<div class="saying">
			Nothing is impossible, Everything is possible!
		</div>
	</div>
</template>

<script>
	export default{
		name:'footer'
	}
</script>

<style lang="scss">
	.footer {
		float: left;
		width: 100%;
		font-weight: bold;
		font-style: oblique;
		text-align: center;
		color: black;
		margin-top: 20px;
	
		.saying {
			font-size: 20px;
			margin-bottom: 20px;
		}
	
		.visit {
			font-size: 15px;
			
		}
	}
</style>
