from flask import *
from datetime import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        climate_zone = request.form.get('climate-zone')
        return redirect(url_for(
            'result',
            climate_zone=climate_zone))
    return render_template(
        "home.html",
        year=datetime.today().year
        )

@app.route('/result', methods=['POST'])
def result():
    place = request.form.get('place')
    type = request.form.get('type')
    year = datetime.today().year
    
    avrgTempNow = (int(request.form.get('maxTempNow')) + int(request.form.get('minTempNow')))/2
    avrgTempLast1Year = (int(request.form.get('maxTempLast1Year')) + int(request.form.get('minTempLast1Year')))/2
    avrgTempLast2Year = (int(request.form.get('maxTempLast2Year')) + int(request.form.get('minTempLast2Year')))/2
    avrgTempLast3Year = (int(request.form.get('maxTempLast3Year')) + int(request.form.get('minTempLast3Year')))/2
    avrgTempLast4Year = (int(request.form.get('maxTempLast4Year')) + int(request.form.get('minTempLast4Year')))/2
    changeTemp1 = avrgTempNow - avrgTempLast1Year
    changeTemp2 = avrgTempLast1Year - avrgTempLast2Year
    changeTemp3 = avrgTempLast2Year - avrgTempLast3Year
    changeTemp4 = avrgTempLast3Year - avrgTempLast4Year
    if avrgTempNow > avrgTempLast1Year:
        processTemp = "Потепління"
    else:
        processTemp = "Замороження"
    dangerTemp = ""
    aboutTempProcess = ""
    normalChangeTemp = 3
    if abs(changeTemp1) >= normalChangeTemp:
        dangerTemp = "Так"
        if changeTemp1 > 0:
            aboutTempProcess = "Це може буди через підвищення концентрації вуглекислого газу в атмосфері, зменшення лісових масивів, промислові викиди та використання викопного палива. Для попередження необхідно: скоротити викиди парникових газів, впроваджувати відновлювані джерела енергії, збільшувати площі лісів та зменшувати споживання викопного палива."
        else:
            aboutTempProcess = "Це може бути через зміни океанських течій, виверження вулканів, зменшення сонячної активності та збільшення кількості аерозолів у повітрі. Для попередження необхідно: контролювати викиди аерозолів та вести спостереження за активністю вулканів. Слід також враховувати можливі наслідки, такі як зміна погодних умов та підвищення попиту на енергоресурси для обігріву."
    else:
        dangerTemp = "Ні"
        if changeTemp1 > 0:
            aboutTempProcess = "Температура підвищується, але це не є критичним. Проте, у разі подальшого підвищення, слід звернути увагу на можливі причини: збільшення промислових викидів, вирубка лісів та підвищення рівня парникових газів. Щоб запобігти негативним наслідкам, варто підтримувати екологічну рівновагу шляхом скорочення викидів, збільшення площі лісів та впровадження технологій із низьким рівнем вуглецевих викидів."
        else:
            aboutTempProcess = "Температура знижується, але це не є критичним. Можливими причинами є природні кліматичні цикли або тимчасові зміни у сонячній активності. Якщо ситуація погіршиться, необхідно спостерігати за змінами в океанських течіях та рівнем аерозолів в атмосфері. Попередити негативні наслідки можна шляхом моніторингу кліматичних змін та інформування населення про можливі ризики."
    

    avrgMoistureNow = (int(request.form.get('maxMoistureNow')) + int(request.form.get('minMoistureNow')))/2
    avrgMoistureLast1Year = (int(request.form.get('maxMoistureLast1Year')) + int(request.form.get('minMoistureLast1Year')))/2
    avrgMoistureLast2Year = (int(request.form.get('maxMoistureLast2Year')) + int(request.form.get('minMoistureLast2Year')))/2
    avrgMoistureLast3Year = (int(request.form.get('maxMoistureLast3Year')) + int(request.form.get('minMoistureLast3Year')))/2
    avrgMoistureLast4Year = (int(request.form.get('maxMoistureLast4Year')) + int(request.form.get('minMoistureLast4Year')))/2
    changeMoisture1 = avrgMoistureNow - avrgMoistureLast1Year
    changeMoisture2 = avrgMoistureLast1Year - avrgMoistureLast2Year
    changeMoisture3 = avrgMoistureLast2Year - avrgMoistureLast3Year
    changeMoisture4 = avrgMoistureLast3Year - avrgMoistureLast4Year
    if avrgMoistureNow > avrgMoistureLast1Year:
        processMoisture = "Збільшення"
    else:
        processMoisture = "Зменшення"
    dangerMoisture = ""
    aboutMoistureProcess = ""
    normalChangeMoisture = 3
    if abs(changeMoisture1) >= normalChangeMoisture:
        dangerMoisture = "Так"
        if changeMoisture1 > 0:
            aboutMoistureProcess = "Це пов'язано з підвищенням кількості опадів, зменшення випаровування через зниження температури, зміни у водному циклі. Це може призвести до підвищення рівня ґрунтових вод, ризик підтоплення територій, зниження врожайності деяких культур. Для запобігання слід: покращити дренажну систему, проводити спостереження за рівнем ґрунтових вод та уникати надмірного зрошення полів."
        else:
            aboutMoistureProcess = "Це пов'язано зі зменшенням кількості опадів, підвищенням температури повітря, збільшенням випаровування та тривалими посухами. Це може призвести до деградації ґрунту, зменшення врожайності сільськогосподарських культур, виникнення пилових бур. Для запобігання слід: впроваджувати системи крапельного зрошення, зберігати вологу у ґрунті шляхом мульчування та проводити збір дощової води для подальшого використання."
    else:
        dangerMoisture = "Ні"
        if changeMoisture1 > 0:
            aboutMoistureProcess = "Це пов'язано зі збільшенням кількості опадів або зменшенням випаровування. Це може бути нормальним процесом, але у разі тривалого підвищення існує ризик підтоплення територій та підвищення рівня ґрунтових вод. Для запобігання слід контролювати дренажну систему, стежити за рівнем ґрунтових вод та уникати надмірного зрошення полів."
        else:
            aboutMoistureProcess = "Це пов'язано з тимчасовим зменшенням кількості опадів або збільшенням випаровування. Це може бути природним процесом, але тривале зменшення може спричинити висихання ґрунту та зменшення врожайності. Для запобігання слід проводити моніторинг рівня вологості ґрунту, застосовувати методи збереження вологи та забезпечити ефективне використання систем зрошення."
    
    avrgPressureNow = (int(request.form.get('maxPressureNow')) + int(request.form.get('minPressureNow')))/2
    avrgPressureLast1Year = (int(request.form.get('maxPressureLast1Year')) + int(request.form.get('minPressureLast1Year')))/2
    avrgPressureLast2Year = (int(request.form.get('maxPressureLast2Year')) + int(request.form.get('minPressureLast2Year')))/2
    avrgPressureLast3Year = (int(request.form.get('maxPressureLast3Year')) + int(request.form.get('minPressureLast3Year')))/2
    avrgPressureLast4Year = (int(request.form.get('maxPressureLast4Year')) + int(request.form.get('minPressureLast4Year')))/2
    changePressure1 = avrgPressureNow - avrgPressureLast1Year
    changePressure2 = avrgPressureLast1Year - avrgPressureLast2Year
    changePressure3 = avrgPressureLast2Year - avrgPressureLast3Year
    changePressure4 = avrgPressureLast3Year - avrgPressureLast4Year
    if avrgPressureNow > avrgPressureLast1Year:
        processPressure = "Збільшення"
    else:
        processPressure = "Зменшення"
    dangerPressure = ""
    aboutPressureProcess = ""
    normalChangePressure = 3
    if abs(changePressure1) >= normalChangePressure:
        dangerPressure = "Так"
        if changePressure1 > 0:
            aboutPressureProcess = "Збільшення атмосферного тиску може бути пов'язане з посиленням антициклонів або зростанням температури повітря. Наслідки можуть включати підвищення ймовірності посух, зменшення кількості опадів та погіршення самопочуття у метеочутливих людей. Рекомендації: стежити за прогнозом погоди, зволожувати повітря в приміщеннях, а метеочутливим людям — уникати надмірного фізичного навантаження."
        else:
            aboutPressureProcess = "Зменшення атмосферного тиску може бути спричинене наближенням циклону або змінами погоди (підвищення вологості, збільшення кількості опадів). Це може викликати погіршення самопочуття у людей, збільшення кількості опадів та посилення вітру. Рекомендації: за можливості залишатися вдома у разі штормового попередження та забезпечити підготовку до опадів або сильного вітру."
    else:
        dangerPressure = "Ні"
        if changePressure1 > 0:
            aboutPressureProcess = "Незначне збільшення атмосферного тиску може бути наслідком природних змін у погодних умовах або переходом від циклонів до антициклонів. Наслідки зазвичай мінімальні, але для метеочутливих людей це може спричиняти легке погіршення самопочуття. Рекомендації: для метеочутливих людей — зволожувати повітря у приміщеннях та уникати фізичних навантажень."
        else:
            aboutPressureProcess = "Незначне зменшення атмосферного тиску може бути спричинене сезонними змінами або слабким впливом циклонів. Наслідки зазвичай обмежуються невеликим посиленням вітру або збільшенням вологості. Рекомендації: слідкувати за прогнозом погоди та уникати поїздок у відкритій місцевості під час сильного вітру."
    

    avrgAmountCO2Now = int(request.form.get('avrgAmountCO2Now'))
    avrgAmountCO2Last1Year = int(request.form.get('avrgAmountCO2Last1Year'))
    avrgAmountCO2Last2Year = int(request.form.get('avrgAmountCO2Last2Year'))
    avrgAmountCO2Last3Year = int(request.form.get('avrgAmountCO2Last3Year'))
    avrgAmountCO2Last4Year = int(request.form.get('avrgAmountCO2Last4Year'))
    changeAmountCO21 = avrgAmountCO2Now - avrgAmountCO2Last1Year
    changeAmountCO22 = avrgAmountCO2Last1Year - avrgAmountCO2Last2Year
    changeAmountCO23 = avrgAmountCO2Last2Year - avrgAmountCO2Last3Year
    changeAmountCO24 = avrgAmountCO2Last3Year - avrgAmountCO2Last4Year
    if avrgAmountCO2Now > avrgAmountCO2Last1Year:
        processAmountCO2 = "Збільшення"
    else:
        processAmountCO2 = "Зменшення"
    dangerAmountCO2 = ""
    aboutAmountCO2Process = ""
    normalChangeAmountCO2 = 3
    if abs(changeAmountCO21) >= normalChangeAmountCO2:
        if changeAmountCO21 > 0:
            aboutAmountCO2Process = "Це може бути пов'язано зі збільшенням спалювання викопного палива, вирубкою лісів та зменшенням здатності рослин до поглинання CO₂. Наслідки включають посилення парникового ефекту, зміну клімату та підвищення середньої глобальної температури. Для зменшення рівня CO₂ слід: зменшити використання викопного палива, збільшити площу лісів, застосовувати екологічно чисті джерела енергії."
            dangerAmountCO2 = "Так"
        else:
            aboutAmountCO2Process = "Зменшення кількості CO₂ може бути спричинене збільшенням поглинання CO₂ рослинами або зниженням викидів завдяки використанню екологічних технологій. Це позитивний процес, який може сприяти зменшенню парникового ефекту та покращенню кліматичної ситуації. Для підтримання цього процесу слід: продовжувати впроваджувати екологічно чисті технології та підтримувати програми збереження лісів."
            dangerAmountCO2 = "Ні"
    else:
        dangerAmountCO2 = "Ні"
        if changeAmountCO21 > 0:
            aboutAmountCO2Process = "Незначне збільшення кількості CO₂ може бути пов'язане зі сезонними коливаннями у здатності рослин поглинати CO₂ або незначним зростанням викидів. Це може мати мінімальний вплив на клімат, але за тривалого збільшення можливе посилення парникового ефекту. Для запобігання слід контролювати викиди CO₂ та сприяти збереженню лісів."
        else:
            aboutAmountCO2Process = "Незначне зменшення кількості CO₂ може бути наслідком сезонних змін у здатності рослин поглинати CO₂ або впровадженням екологічних технологій. Це позитивний процес, який свідчить про можливість зниження парникового ефекту. Для підтримання цього слід продовжувати використовувати екологічно чисті технології та підтримувати програми збереження лісів."
    
    print(aboutAmountCO2Process)
    print(aboutMoistureProcess)

    return render_template(
        'result.html', 
        place=place, 
        year=year,
        processTemp=processTemp,
        dangerTemp=dangerTemp,
        aboutTempProcess=aboutTempProcess,
        avrgTempNow=avrgTempNow,
        avrgTempLast1Year=avrgTempLast1Year,
        avrgTempLast2Year=avrgTempLast2Year,
        avrgTempLast3Year=avrgTempLast3Year,
        avrgTempLast4Year=avrgTempLast4Year,
        changeTemp1=changeTemp1,
        changeTemp2=changeTemp2,
        changeTemp3=changeTemp3,
        changeTemp4=changeTemp4,

        processMoisture=processMoisture,
        dangerMoisture=dangerMoisture,
        aboutMoistureProcess=aboutMoistureProcess,
        avrgMoistureNow=avrgMoistureNow,
        avrgMoistureLast1Year=avrgMoistureLast1Year,
        avrgMoistureLast2Year=avrgMoistureLast2Year,
        avrgMoistureLast3Year=avrgMoistureLast3Year,
        avrgMoistureLast4Year=avrgMoistureLast4Year,
        changeMoisture1=changeMoisture1,
        changeMoisture2=changeMoisture2,
        changeMoisture3=changeMoisture3,
        changeMoisture4=changeMoisture4,

        processPressure=processPressure,
        dangerPressure=dangerPressure,
        aboutPressureProcess=aboutPressureProcess,
        avrgPressureNow=avrgPressureNow,
        avrgPressureLast1Year=avrgPressureLast1Year,
        avrgPressureLast2Year=avrgPressureLast2Year,
        avrgPressureLast3Year=avrgPressureLast3Year,
        avrgPressureLast4Year=avrgPressureLast4Year,
        changePressure1=changePressure1,
        changePressure2=changePressure2,
        changePressure3=changePressure3,
        changePressure4=changePressure4,

        processAmountCO2=processAmountCO2,
        dangerAmountCO2=dangerAmountCO2,
        aboutAmountCO2Process=aboutAmountCO2Process,
        avrgAmountCO2Now=avrgAmountCO2Now,
        avrgAmountCO2Last1Year=avrgAmountCO2Last1Year,
        avrgAmountCO2Last2Year=avrgAmountCO2Last2Year,
        avrgAmountCO2Last3Year=avrgAmountCO2Last3Year,
        avrgAmountCO2Last4Year=avrgAmountCO2Last4Year,
        changeAmountCO21=changeAmountCO21,
        changeAmountCO22=changeAmountCO22,
        changeAmountCO23=changeAmountCO23,
        changeAmountCO24=changeAmountCO24
    )

if __name__ == "__main__":
    app.run(debug=True)