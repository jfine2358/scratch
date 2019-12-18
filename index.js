// TODO: Understand, refactor and clean up this code.

// Based on code on page http://asciimath.org/
window.MathJax = {

    "fast-preview": {
	disabled: true
    },

    AuthorInit: function() {
	MathJax.Hub.Register.StartupHook('End', function() {

	    MathJax.Hub.processSectionDelay = 0

	    // Get nodes src and jax.
	    var src = document.getElementById('src')
	    var tgt = document.getElementById('tgt')
	    var jax = MathJax.Hub.getAllJax(tgt)[0]

	    // Have input at src queue update on jax.
	    src.addEventListener('input', function() {
	      MathJax.Hub.Queue(['Text', jax, src.value])
	    })

	})
    }
}
