#include <fcntl.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h> 
#include <stdlib.h>
#include <string.h>

#define MAX_BUF 1024

int  main()
{
	system("clear");
	
	int fdw, fdr, i, selectionMenu = 0;
	char buf[MAX_BUF];
	char* textInitCon = "hello";
	char* myfifow = "ctopyfifo";
	char* myfifor = "pytocfifo";

	const char* choix[5][2];

	choix[0][0] = "A1f2G7";
	choix[0][1] = "Serge Junsenbergerr";
	choix[1][0] = "weq814";
	choix[1][1] = "Police du Lac";
	choix[2][0] = "5zjtR2";
	choix[2][1] = "Bob the Eponges";
	choix[3][0] = "Hbid13";
	choix[3][1] = "John Doe";
	choix[4][0] = "zuR5c4";
	choix[4][1] = "Toupille Attaque";

	/* Create fifos */
	mkfifo(myfifow,0666); 
	mkfifo(myfifor,0666);
		
	/* Send Hi to pipe */
	printf("Writing init string TO pipe: >> %s << ...\n", textInitCon);
	fdw = open(myfifow, O_WRONLY);
	write(fdw, textInitCon, sizeof(textInitCon));
	close(fdw);

	/* Wait Ok from pipe */
/*	fdr = open(myfifor, O_RDONLY);
	read(fdr, buf, MAX_BUF);
	printf("Received init string FROM pipe: >> %s << ...\n", buf);
	close(fdr);
*/
	
//	if (strcmp(buf, "Ok") == 0) {
		printf("Init ok, start pushing ...\n\n");
		
		/* Print menu */
		printf("Index\tID\tPerson\n");
		printf("-----\t--\t------\n\n");
		
		/* print selection list */
		for (i = 0; i < 5; i++) {
				printf("%d\t%s\t%s\n",i, choix[i][0], choix[i][1]);
		}
		
		printf("\n");
		
		while (selectionMenu != 8) {
			printf("Type index, 8 to quit: ");
			scanf("%d", &selectionMenu);
			
			if (selectionMenu != 8) {
				printf("Writing: >> %s << to pipe...\n", choix[selectionMenu][0]);
				fdw = open(myfifow, O_WRONLY);
				write(fdw, choix[selectionMenu][0], strlen(choix[selectionMenu][0]));
				close(fdw);
			} else {
				printf("Writing: >> %s << to pipe...\n", "8");
				fdw = open(myfifow, O_WRONLY);
				write(fdw, "8", strlen("8"));
				close(fdw);				
			}
			
/*			fdr = open(myfifor, O_RDONLY);
			read(fdr, buf, MAX_BUF);
			printf("Received string FROM pipe: >> %s << ...\n", buf);
			close(fdr);
*/
		  
		}
		
		printf("\nstop pushing ... program terminated!\n\n");
		
/*	} else {
		printf("Init failed, abort!\n");
	}
*/
	
	/* Remove fifos */
	unlink(myfifow);
	unlink(myfifor);
	
	return 0;
}

