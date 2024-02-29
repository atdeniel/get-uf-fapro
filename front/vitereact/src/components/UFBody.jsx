import DatePicker from 'react-datepicker';
import { useState, useEffect } from 'react'
import { format, parse } from 'date-fns';

function UFBody() {

    const [date, setDate] = useState(new Date());
    const [ufInfo, setUfInfo] = useState();
    const minDate = new Date('2013-01-01');
    const maxDate = new Date();
    const strDateFormat = 'dd-MM-yyyy'

    /**
     * Maneja el cambio de la fecha seleccionada en el componente de fecha. Actualiza el estado de la fecha
     * con el nuevo valor y realiza una llamada a la API con la fecha formateada.
     *
     * @param {Date} date - La nueva fecha seleccionada por el usuario.
     */
    const handleDateChange = (date) => {
        setDate(date);
        const formattedDate = format(date, strDateFormat);
        fetchApiData(formattedDate);
    };

    /**
     * Maneja el cambio de la fecha a través de un input directo del usuario.
     * Ignora los eventos desencadenados por clics como al seleccionar la fecha en el calendario. Si el valor ingresado
     * es una fecha válida dentro del rango permitido, actualiza el estado con la nueva fecha, formatea la fecha y
     * realiza una llamada a la API con la fecha formateada.
     *
     * @param {Event} event - El evento desencadenado por el cambio en el input de fecha.
     */
    const handleDateChangeRaw = (event) => {
        if (event.type === 'click') return;
        const date = parse(event.target.value, strDateFormat, new Date());
        if (!isNaN(date) && date >= minDate && date <= maxDate) {
            setDate(date);
            const formattedDate = format(date, strDateFormat);
            fetchApiData(formattedDate);
        }
    };

    /**
     * Realiza una solicitud asincrónica a una API para obtener información del valor de la UF a partir de la fecha
     * proporcionada. Construye la URL de la API utilizando una variable de entorno para la base de la URL y añade la
     * fecha como parámetro de consulta. Si la solicitud es exitosa, actualiza el estado con la información obtenida.
     * En caso de error, registra el error en la consola.
     *
     * @param {string} date - La fecha para la cual se solicitan los datos, formateada como una cadena de texto. El
     * formato debiese ser como strDateFormat (dd-MM-yyyy)
     */
    const fetchApiData = async (date) => {
        const apiUrl = `${import.meta.env.VITE_SII_UF_API_URL}?date=${date}`;
        try {
            const response = await fetch(apiUrl);
            const data = await response.json();
            setUfInfo(data)
        } catch (error) {
            console.error("Hubo un error al obtener los datos de la API:", error);
        }
    };

    /**
     * useEffect para inicializar el componente con datos de la fecha actual.
     *
     */
    useEffect(() => {
        handleDateChange(new Date());
    }, []);


    return (
        <div className="ufDate__form--classic">
            <div className="App">
                <DatePicker
                    selected={date}
                    onChange={handleDateChange}
                    onChangeRaw={handleDateChangeRaw}
                    dateFormat={strDateFormat}
                    isClearable
                    showYearDropdown
                    scrollableMonthYearDropdown
                    minDate={minDate}
                    maxDate={maxDate}
                />
            </div>

            <div className="ufValueBody">
                <br></br>
                {ufInfo && ufInfo.uf_value ? (
                    <h1 className="ufValue--text bottom">${ufInfo.uf_value}</h1>
                ):(
                    <h2>Sin información</h2>
                )}
            </div>
        </div>
    )
}

export default UFBody