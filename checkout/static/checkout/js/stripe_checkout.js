
var stripePublicKey = $("#id_stripe_public_key").text().slice(1,-1);
var clientSecret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey);
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

var form = document.getElementById('checkout-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    stripeCard.update({ 'disabled': true});
    $('#submit-btn').attr('disabled', true);
    $('#checkout-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: stripeCard,
            billing_details: {
                name: $.trim(form.name.value),
                phone: $.trim(form.phone.value),
                email: $.trim(form.email.value),
                address: {
                    line1 : $.trim(form.address_line_1.value),
                    line2: $.trim(form.address_line_2.value),
                    city: $.trim(form.city.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                

            }
        }
    },
            shipping: {
                name: $.trim(form.name.value),
                phone: $.trim(form.phone.value),
                address: {
                    line1 : $.trim(form.address_line_1.value),
                    line2: $.trim(form.address_line_2.value),
                    city: $.trim(form.city.value),
                    postal_code: $.trim(form.postcode.value),
                    country: $.trim(form.country.value),
                
            }
    },
}).then(function(result) {
        if (result.error) {
            var cardError = document.getElementById('card-error-message');
            var html = `
                <span>${result.error.message}</span>`;
            $(cardError).html(html);
            $('#checkout-form').fadeToggle(100);
            $('#loading-overlay').fadeToggle(100);
            stripeCard.update({ 'disabled': false});
            $('#submit-btn').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    })
})