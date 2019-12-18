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


var examples = [
    '2 + 2 = 4',
    '\\alpha',
    '\\frac{1}{2}',
];

examples.ptr = -1


var next = document.getElementById('next').onclick = (
    function(){

	examples.ptr = (examples.ptr + 1) % examples.length;
	example = examples[examples.ptr]
	document.getElementById('src0').value = example;

	var tgt = document.getElementById('tgt0');
	var jax = MathJax.Hub.getAllJax(tgt)[0]
	MathJax.Hub.Queue(['Text', jax, example])

	document.getElementById('src').value = '';
	document.getElementById('src').dispatchEvent(
	    new Event('input', { bubbles: true })
	);

    }
)
