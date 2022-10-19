
var stripe_public_key = $("#id_stripe_public_key").text().slice(1,-1);
var client_secret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripe_public_key);
var elements = stripe.elements();

var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var stripeCard = elements.create('card', {
    style: style });
    stripeCard.mount('#stripe-card');


stripeCard.addEventListener('change', function (event) {
    var cardError = document.getElementById('card-error-message');
    if (event.error) {

        var html = `
            <span>${event.error.message}</span>`;
        $(cardError).html(html);
    } else {
        cardError.textContent = '';
    }
});

// stripe documentation

