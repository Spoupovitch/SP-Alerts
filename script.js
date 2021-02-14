document.onload(function() {
    while(true) {

        setTimeout(function() {
            
            $.ajax({
                type: "POST",
                url: "*.py"
            }).done(priceChanges => {
                console.log(priceChanges);
            });

        }, 1000 * 60)
    }
});