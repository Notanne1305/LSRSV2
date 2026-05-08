/** @type {import('tailwindcss').Config} */
export default {
    darkMode: 'class',
    content: [
        './resources/**/*.blade.php',
        './resources/**/*.js',
        './resources/**/*.vue',
    ],
    theme: {
        extend: {
            fontFamily: {
                'colonna': ['Colonna Regular', 'serif'],
                'pristina': ['Pristina Black', 'serif'],
                'harmonia': ['Harmonia Sans W01 Regular', 'sans-serif'],
            },
        },
    },
    plugins: [],
}
