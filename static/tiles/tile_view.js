
// Listen for click on toggle checkbox
$('#select-all').click(function(event) {   
    if(this.checked) {
        // Iterate each checkbox
        $('.subtiles :checkbox').each(function() {
            this.checked = true;                        
        });
    } else {
        $('.subtiles :checkbox').each(function() {
            this.checked = false;                       
        });
    }
}); 
