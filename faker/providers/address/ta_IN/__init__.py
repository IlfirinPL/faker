# coding=utf-8
from __future__ import unicode_literals

from .. import Provider as AddressProvider


class Provider(AddressProvider):

    city_formats = ('{{city_name}}', )

    street_name_formats = (
        '{{first_name}} {{last_name}}',
        '{{last_name}}',
    )

    street_address_formats = ('{{building_number}} {{street_name}}', )

    address_formats = ('{{street_address}}\n{{city}} {{postcode}}',
                       '{{street_address}}\n{{city}}-{{postcode}}')

    building_number_formats = (
        '####', '###', '##', '#', '#/#', '##/##', '##/###', '##/####')

    postcode_formats = ('######', )

    # Source: https://ta.wikipedia.org/wiki/மக்கள்_தொகை_மிகுந்த_இந்திய_நகரங்கள்
    cities = (
        'சென்னை',
        'கோயம்புத்தூர்',
        'மதுரை',
        'திருச்சிராப்பள்ளி',
        'திருப்பூர்',
        'சேலம்',
        'ஈரோடு',
        'திருநெல்வேலி',
        'வேலூர்',
        'தூத்துக்குடி',
        'திண்டுக்கல்',
        'தஞ்சாவூர்',
        'இராணிப்பேட்டை',
        'சிவகாசி',
        'கரூர் (கரூர் மாவட்டம்)',
        'உதகமண்டலம்',
        'ஓசூர்',
        'நாகர்கோவில்',
        'காஞ்சிபுரம்',
        'குமாரபாளையம்',
        'காரைக்குடி',
        'நெய்வேலி',
        'கடலூர்',
        'கும்பகோணம்',
        'திருவண்ணாமலை',
        'பொள்ளாச்சி',
        'இராஜபாளையம், விருதுநகர் மாவட்டம்',
        'குடியாத்தம்',
        'புதுக்கோட்டை',
        'வாணியம்பாடி',
        'ஆம்பூர்',
        'நாகப்பட்டினம்',
        'மும்பை பெருநகர்',
        'தில்லி',
        'கொல்கத்தா பெருநகர்',
        'சென்னை பெருநகர்',
        'பெங்களூரு',
        'ஐதராபாத்',
        'புனே',
        'அகமதாபாத்',
        'கான்பூர்',
        'சூரத்',
        'ஜெய்ப்பூர்',
        'லக்னோ',
        'பாட்னா',
        'நாக்பூர்',
        'இந்தோர்',
        'மீரட்',
        'நாசிக்',
        'போபால்',
        'லூதியானா',
        'ஆக்ரா',
        'வதோதரா',
        'புவனேசுவர்',
        'கோயம்புத்தூர்',
        'ராஜ்கோட்',
        'கொச்சி',
        'விசாகப்பட்டினம்',
        'வாரணாசி',
        'மதுரை',
        'ஆசன்சோல்',
        'அலகாபாத்',
        'மைசூர்',
        'ஜபல்பூர்',
        'ஜம்சேத்பூர்',
        'அவுரங்கபாத்',
        'அம்ரித்சர்',
        'தன்பாத்',
        'விஜயவாடா',
        'சோலாப்பூர்',
        'பிலாய்',
        'ஸ்ரீநகர்',
        'ராஞ்சி',
        'திருவனந்தபுரம்',
        'சண்டிகர்',
        'குவஹாத்தி',
        'கோழிக்கோடு',
        'ஜோத்பூர்',
        'குவாலியர்',
        'ஜலந்தர்',
        'திருச்சிராப்பள்ளி',
        'பரேலி',
        'ஹுப்ளி-தர்வாத்',
        'அலிகார்',
        'கோட்டா',
        'மொரதாபாத்',
        'ராய்ப்பூர்',
        'தேராதூன்',
        'கோரக்பூர்',
        'ஜம்மு',
        'அமராவதி',
        'வாரங்கல்',
        'ஜாம்நகர்',
        'பிகானேர்',
        'சாங்கலி',
        'திருப்பூர்',
        'பாவ்நகர்',
        'மங்களூர்',
        'அஜ்மீர்',
        'பொகாரோ',
        'பெல்காம்',
        'புதுச்சேரி',
        'சிலிகுரி',
        'கண்ணூர்',
        'கோலாப்பூர்',
        'நான்தேட்',
        'ரூர்கேலா',
        'துர்காபூர்',
        'குல்பர்கா',
        'குண்டூர்',
        'ஜான்சி',
        'சகாரன்பூர்',
        'கரக்பூர்',
        'கயா',
        'ஜல்கான்',
        'மதுரா',
        'கொல்லம்',
        'கோர்பா',
        'பிரோசாபாத்',
        'திருநெல்வேலி',
        'உஜ்ஜைன்',
        'அகமத்நகர்',
        'நெல்லூர்',
        'ராமகுண்டம்',
        'ராஜமுந்திரி',
        'மாலேகான்',
        'உதயப்பூர்',
        'அகோலா',
        'தாவண்கரே',
        'வேலூர்',
        'திருவண்ணாமலை',
        'காஜுவாகா',
    )

    # Source: https://ta.wikipedia.org/wiki/இந்தியாவின்_மாநிலங்களும்_ஆட்சிப்பகுதிகளும்
    states = (
        'ஆந்திரப் பிரதேசம்',
        'அருணாச்சலப் பிரதேசம்',
        'அசாம்',
        'பீகார்',
        'சத்தீஸ்கர்',
        'கோவா',
        'குஜராத்',
        'அரியானா',
        'இமாச்சலப் பிரதேசம்',
        'சம்மு காசுமீர்',
        'ஜார்கண்ட்',
        'கர்நாடகா',
        'கேரளா',
        'மத்தியப் பிரதேசம்',
        'மகாராஷ்டிரா',
        'மணிப்பூர்',
        'மேகாலயா',
        'மிசோரம்',
        'நாகலாந்து',
        'ஒரிசா',
        'பஞ்சாப்',
        'ராஜஸ்தான்',
        'சிக்கிம்',
        'தமிழ்நாடு',
        'தெலுங்கானா',
        'திரிபுரா',
        'உத்தரப்பிரதேசம்',
        'உத்தரகண்ட்',
        'மேற்கு வங்கம்',
    )

    # Source: https://ta.wikipedia.org/wiki/பிறப்பு_விகித_அடிப்படையில்_நாடுகளின்_பட்டியல்
    countries = (
        'ஆப்கானித்தான்',
        'அல்பேனியா',
        'அல்ஜீரியா',
        'அந்தோரா',
        'அங்கோலா',
        'அன்டிகுவா பர்புடா',
        'அர்கெந்தீனா',
        'ஆர்மீனியா',
        'ஆத்திரேலியா',
        'ஆஸ்திரியா',
        'அசர்பைஜான்',
        'பஹமாஸ்',
        'பகுரைன்',
        'வங்காளதேசம்',
        'பார்படோசு',
        'பெலருஸ்',
        'பெல்ஜியம்',
        'பெலீசு',
        'பெனின்',
        'பூட்டான்',
        'பொலிவியா',
        'பொசுனியா எர்செகோவினா',
        'போட்சுவானா',
        'பிரேசில்',
        'புரூணை',
        'பல்கேரியா',
        'புர்க்கினா பாசோ',
        'புருண்டி',
        'கம்போடியா',
        'கமரூன்',
        'கனடா',
        'கேப் வர்டி',
        'மத்திய ஆப்பிரிக்கக் குடியரசு',
        'சாட்',
        'சிலி',
        'சீனா',
        'கொலம்பியா',
        'கொமொரோசு',
        'காங்கோ மக்களாட்சிக் குடியரசு',
        'காங்கோ மக்களாட்சிக் குடியரசு',
        'கோஸ்ட்டா ரிக்கா',
        'ஐவரி கோஸ்ட்',
        'குரோவாசியா',
        'கியூபா',
        'சைப்பிரசு',
        'செக் குடியரசு',
        'டென்மார்க்',
        'சீபூத்தீ',
        'டொமினிக்கா',
        'டொமினிக்கன் குடியரசு',
        'எக்குவடோர்',
        'எகிப்து',
        'எல் சல்வடோர',
        'எக்குவடோரியல் கினி',
        'எரித்திரியா',
        'எசுத்தோனியா',
        'எதியோப்பியா',
        'பிஜி',
        'பின்லாந்து',
        'பிரான்சு',
        'காபொன்',
        'கம்பியா',
        'சியார்சியா',
        'செருமனி',
        'கானா',
        'கிரேக்க நாடு',
        'கிரெனடா',
        'குவாத்தமாலா',
        'கினியா',
        'கினி-பிசாவு',
        'கயானா',
        'எயிட்டி',
        'ஒண்டுராசு',
        'அங்கேரி',
        'ஐசுலாந்து',
        'இந்தியா',
        'இந்தோனேசியா',
        'ஈரான்',
        'ஈராக்',
        'அயர்லாந்து',
        'இசுரேல்',
        'இத்தாலி',
        'ஜமேக்கா',
        'சப்பான்',
        'யோர்தான்',
        'கசக்கஸ்தான்',
        'கென்யா',
        'கிரிபட்டி',
        'வட கொரியா',
        'தென் கொரியா',
        'குவைத்',
        'கிர்கிசுத்தான்',
        'லாவோஸ்',
        'லாத்வியா',
        'லெபனான்',
        'லெசோத்தோ',
        'லைபீரியா',
        'லிபியா',
        'லீக்கின்ஸ்டைன்',
        'லித்துவேனியா',
        'லக்சம்பர்க்',
        'மாக்கடோனியக் குடியரசு',
        'மடகாசுகர்',
        'மலாவி',
        'மலேசியா',
        'மாலைத்தீவுகள்',
        'மாலி',
        'மால்ட்டா',
        'மார்சல் தீவுகள்',
        'மூரித்தானியா',
        'மொரிசியசு',
        'மெக்சிக்கோ',
        'மைக்குரோனீசியக் கூட்டு நாடுகள்',
        'மல்தோவா',
        'மொனாகோ',
        'மங்கோலியா',
        'மொண்டெனேகுரோ',
        'மொரோக்கோ',
        'மொசாம்பிக்',
        'மியான்மர்',
        'நமீபியா',
        'நவூரு',
        'நேபாளம்',
        'நெதர்லாந்து',
        'நியூசிலாந்து',
        'நிக்கராகுவா',
        'நைஜர்',
        'நைஜீரியா',
        'நோர்வே',
        'ஓமான்',
        'பாக்கித்தான்',
        'பலாவு',
        'பலத்தீன்',
        'பனாமா',
        'பப்புவா நியூ கினி',
        'பரகுவை',
        'பெரு',
        'பிலிப்பீன்சு',
        'போலந்து',
        'போர்த்துகல்',
        'கட்டார்',
        'உருமேனியா',
        'உருசியா',
        'ருவாண்டா',
        'செயிண்ட். கிட்ஸ் நெவிஸ்',
        'செயிண்ட். லூசியா',
        'செயின்ட் வின்செண்டு மற்றும் கிரெனடீன்கள்',
        'சமோவா',
        'சான் மரீனோ',
        'சாவோ தொமே மற்றும் பிரின்சிப்பி',
        'சவூதி அரேபியா',
        'செனிகல்',
        'செர்பியா',
        'சீசெல்சு',
        'சியேரா லியோனி',
        'சிங்கப்பூர்',
        'சிலவாக்கியா',
        'சுலோவீனியா',
        'சொலமன் தீவுகள்',
        'சோமாலியா',
        'தென்னாப்பிரிக்கா',
        'தெற்கு சூடான்',
        'எசுப்பானியா',
        'இலங்கை',
        'சூடான்',
        'சுரிநாம்',
        'சுவாசிலாந்து',
        'சுவீடன்',
        'சுவிட்சர்லாந்து',
        'சிரியா',
        'சீனக் குடியரசு',
        'தாஜிக்ஸ்தான்',
        'தன்சானியா',
        'தாய்லாந்து',
        'கிழக்குத் திமோர்',
        'டோகோ',
        'தொங்கா',
        'டிரினிடாட் மற்றும் டொபாகோ',
        'தூனிசியா',
        'துருக்கி',
        'துருக்மெனிஸ்தான்',
        'துவாலு',
        'உகாண்டா',
        'உக்ரைன்',
        'ஐக்கிய அரபு அமீரகம்',
        'ஐக்கிய இராச்சியம்',
        'ஐக்கிய அமெரிக்கா',
        'உருகுவை',
        'உஸ்பெகிஸ்தான்',
        'வனுவாட்டு',
        'வெனிசுவேலா',
        'வியட்நாம்',
        'மேற்கு சகாரா (Sahrawi)',
        'யேமன்',
        'சாம்பியா',
        'சிம்பாப்வே',
        'அங்கியுலா (UK)',
        'அரூபா (Netherlands)',
        'பெர்முடா (UK)',
        'கேமன் தீவுகள் (UK)',
        'குயெர்ன்சி (கால்வாய் தீவுகள், UK)',
        'யேர்சி (கால்வாய் தீவுகள், UK)',
        'குக் தீவுகள் (New Zealand)',
        'குராசோ (Netherlands)',
        'போக்லாந்து தீவுகள்/Malvinas',
        'பரோயே தீவுகள் (Denmark)',
        'கிப்ரல்டார் (UK)',
        'கிறீன்லாந்து (Denmark)',
        'குவாதலூப்பு (France)',
        'குவாம் (USA)',
        'பிரெஞ்சு கயானா',
        'ஆங்காங்',
        'மாண் தீவு (UK)',
        'கொசோவோ',
        'மக்காவு',
        'மர்தினிக்கு (France)',
        'மயோட்டே (France)',
        'மொன்செராட்',
    )

    def city_name(self):
        return self.random_element(self.cities)

    def state(self):
        return self.random_element(self.states)
