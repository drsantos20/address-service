

def build_google_maps_url(body, google_api_key):
    street = body['street']
    city = body['city']
    neighborhood = body['neighborhood']
    uf = body['uf']
    street = street.replace(' ', '+')
    city = city.replace(' ', '+')
    neighborhood = neighborhood.replace(' ', '+')
    uf = uf.replace(' ', '+')
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address={}+{}+{}+{}&key={}'.format(
        street,
        neighborhood,
        city,
        uf,
        google_api_key
    )
    return url
