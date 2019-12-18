// TODO: Understand, refactor and clean up this code.

// Based on code on page http://asciimath.org/
window.MathJax = {
    "fast-preview": {
	disabled: true
    },
    AuthorInit: function() {
	MathJax.Hub.Register.StartupHook('End', function() {
	    MathJax.Hub.processSectionDelay = 0
	    var demoSource = document.getElementById('src')
	    var demoRendering = document.getElementById('tgt')
	    var math = MathJax.Hub.getAllJax('tgt')[0]
	    demoSource.addEventListener('input', function() {
	      MathJax.Hub.Queue(['Text', math, demoSource.value])
	    })
	})
    }
}
