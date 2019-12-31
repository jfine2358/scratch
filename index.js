// TODO: Understand, refactor and clean up this code.

// Based on code on page http://asciimath.org/
window.MathJax = {

    "fast-preview": {
	disabled: true
    },

    AuthorInit: function() {
	MathJax.Hub.Register.StartupHook('End', function() {

	    MathJax.Hub.processSectionDelay = 0

	    // Get the next (first) example.
	    next();

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
    'x^2 + y^2 = z^2',
    '\\alpha',
    '\\frac{1}{3} + \\frac{1}{6} =\\frac{1}{2}',
    '\\int_{x=0}^1 x^2 \\, dx = \\frac{x^3}{3}'
];

examples.ptr = -1


var next = function(){

    examples.ptr = (examples.ptr + 1) % examples.length;
    example = examples[examples.ptr]
    document.getElementById('src0').value = example;



    var tgt = document.getElementById('tgt');
    var tgt0 = document.getElementById('tgt0');
    var jax = MathJax.Hub.getAllJax(tgt0)[0];

    // Synchronize height of the render boxes.
    var update_height = function(){
	tgt.style.height = tgt0.offsetHeight;
    }

    MathJax.Hub.Queue(
	['Text', jax, example],
	[update_height]
    );

    document.getElementById('src').value = '';
    document.getElementById('src').dispatchEvent(
	new Event('input', { bubbles: true })
    );

}

document.getElementById('form').onsubmit = next
