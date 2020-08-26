export default{
    saveLeaveMessages(context,LeaveMessages){
        context.commit('saveLeaveMessages',LeaveMessages)
    },
    savewebReadPerson(context,count){
        context.commit('savewebReadPerson',count)
    }
}