window.addEventListener('load', function() {
    new gridjs.Grid({
        columns: [
            "Title",
            {
                name : "Watched", 
                width : "150px",
                sort : "true"
            },
            "Date"
        ],
        pagination: {
            limit: 20
        },
        fixedHeader: true,
        server: {
            url: 'https://serials.danmax.keenetic.link/api',
            then: data => data.map(title => [title.name, title.watched, title.date])
        } 
    }).render(document.getElementById("wrapper"));
});
