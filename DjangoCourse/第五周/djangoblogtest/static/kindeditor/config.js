KindEditor.ready(function (K) {
   window.editor=K.create('#id_content',{
       width:'700px',
       height:'300px',
       uploadJson:'/admin/upload/'
   });
});
