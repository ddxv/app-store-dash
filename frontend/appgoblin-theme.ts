import type { CustomThemeConfig } from '@skeletonlabs/tw-plugin';

export const myCustomTheme: CustomThemeConfig = {
	name: 'appgoblin-theme',
	properties: {
		// =~= Theme Properties =~=
		'--theme-font-family-base': `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'`,
		'--theme-font-family-heading': `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, 'Noto Sans', sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'`,
		'--theme-font-color-base': '0 0 0',
		'--theme-font-color-dark': '255 255 255',
		'--theme-rounded-base': '2px',
		'--theme-rounded-container': '2px',
		'--theme-border-base': '1px',
		// =~= Theme On-X Colors =~=
		'--on-primary': '0 0 0',
		'--on-secondary': '0 0 0',
		'--on-tertiary': '0 0 0',
		'--on-success': '0 0 0',
		'--on-warning': '0 0 0',
		'--on-error': '0 0 0',
		'--on-surface': '0 0 0',
		// =~= Theme Colors  =~=
		// primary | #ccb6e5
		'--color-primary-50': '247 244 251', // #f7f4fb
		'--color-primary-100': '245 240 250', // #f5f0fa
		'--color-primary-200': '242 237 249', // #f2edf9
		'--color-primary-300': '235 226 245', // #ebe2f5
		'--color-primary-400': '219 204 237', // #dbcced
		'--color-primary-500': '204 182 229', // #ccb6e5
		'--color-primary-600': '184 164 206', // #b8a4ce
		'--color-primary-700': '153 137 172', // #9989ac
		'--color-primary-800': '122 109 137', // #7a6d89
		'--color-primary-900': '100 89 112', // #645970
		// secondary | #ffcf96
		'--color-secondary-50': '255 248 239', // #fff8ef
		'--color-secondary-100': '255 245 234', // #fff5ea
		'--color-secondary-200': '255 243 229', // #fff3e5
		'--color-secondary-300': '255 236 213', // #ffecd5
		'--color-secondary-400': '255 221 182', // #ffddb6
		'--color-secondary-500': '255 207 150', // #ffcf96
		'--color-secondary-600': '230 186 135', // #e6ba87
		'--color-secondary-700': '191 155 113', // #bf9b71
		'--color-secondary-800': '153 124 90', // #997c5a
		'--color-secondary-900': '125 101 74', // #7d654a
		// tertiary | #ef53be
		'--color-tertiary-50': '253 229 245', // #fde5f5
		'--color-tertiary-100': '252 221 242', // #fcddf2
		'--color-tertiary-200': '251 212 239', // #fbd4ef
		'--color-tertiary-300': '249 186 229', // #f9bae5
		'--color-tertiary-400': '244 135 210', // #f487d2
		'--color-tertiary-500': '239 83 190', // #ef53be
		'--color-tertiary-600': '215 75 171', // #d74bab
		'--color-tertiary-700': '179 62 143', // #b33e8f
		'--color-tertiary-800': '143 50 114', // #8f3272
		'--color-tertiary-900': '117 41 93', // #75295d
		// success | #99c1f1
		'--color-success-50': '240 246 253', // #f0f6fd
		'--color-success-100': '235 243 252', // #ebf3fc
		'--color-success-200': '230 240 252', // #e6f0fc
		'--color-success-300': '214 230 249', // #d6e6f9
		'--color-success-400': '184 212 245', // #b8d4f5
		'--color-success-500': '153 193 241', // #99c1f1
		'--color-success-600': '138 174 217', // #8aaed9
		'--color-success-700': '115 145 181', // #7391b5
		'--color-success-800': '92 116 145', // #5c7491
		'--color-success-900': '75 95 118', // #4b5f76
		// warning | #fff491
		'--color-warning-50': '255 253 239', // #fffdef
		'--color-warning-100': '255 253 233', // #fffde9
		'--color-warning-200': '255 252 228', // #fffce4
		'--color-warning-300': '255 251 211', // #fffbd3
		'--color-warning-400': '255 247 178', // #fff7b2
		'--color-warning-500': '255 244 145', // #fff491
		'--color-warning-600': '230 220 131', // #e6dc83
		'--color-warning-700': '191 183 109', // #bfb76d
		'--color-warning-800': '153 146 87', // #999257
		'--color-warning-900': '125 120 71', // #7d7847
		// error | #f66151
		'--color-error-50': '254 231 229', // #fee7e5
		'--color-error-100': '253 223 220', // #fddfdc
		'--color-error-200': '253 216 212', // #fdd8d4
		'--color-error-300': '251 192 185', // #fbc0b9
		'--color-error-400': '249 144 133', // #f99085
		'--color-error-500': '246 97 81', // #f66151
		'--color-error-600': '221 87 73', // #dd5749
		'--color-error-700': '185 73 61', // #b9493d
		'--color-error-800': '148 58 49', // #943a31
		'--color-error-900': '121 48 40', // #793028
		// surface | #d9d2dd
		'--color-surface-50': '250 250 250', // #f9f8fa BACKGROUND
		'--color-surface-100': '245 244 245', // #f7f6f8 CARD PANELS
		'--color-surface-200': '240 238 240', // #f6f4f7 TABLE TOPS
		'--color-surface-300': '50 240 250', // #f0edf1
		'--color-surface-400': '200 200 200', // #e4e0e7 SEARCH BAR ICON BACKGROUND
		'--color-surface-500': '212 190 212', // #d9d2dd TABLE ROW DARKER
		'--color-surface-600': '95 189 199', // #c3bdc7
		'--color-surface-700': '63 158 166', // #a39ea6
		'--color-surface-800': '30 126 133', // #827e85
		'--color-surface-900': '06 103 108' // #6a676c
	}
};
