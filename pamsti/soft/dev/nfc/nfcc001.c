/**
 * @file nfcc0xx.c
 * @brief Polling loop that use libnfc
 */

// To compile this file:
// $ gcc -o filename filename.c -lnfc

#ifdef HAVE_CONFIG_H
#  include "config.h"
#endif // HAVE_CONFIG_H

#include <stdlib.h>
#include <err.h>
#include <nfc/nfc.h>

static void
print_hex(const uint8_t *pbtData, const size_t szBytes)
{
  size_t  szPos;

  for (szPos = 0; szPos < szBytes; szPos++) {
    printf("%02x", pbtData[szPos]);
  }
  printf("\n");
}

int
main(int argc, const char *argv[])
{
  system("clear");
  
  nfc_device *pnd;
  nfc_target nt;

  // Allocate only a pointer to nfc_context
  nfc_context *context;

  // Initialize libnfc and set the nfc_context
  nfc_init(&context);

  // Display libnfc version
  const char *acLibnfcVersion = nfc_version();
  printf("%s uses libnfc %s\n", argv[0], acLibnfcVersion);

  // Open, using the first available NFC device.
  pnd = nfc_open(context, NULL);

  if (pnd == NULL) {
    warnx("ERROR: %s", "Unable to open NFC device.");
    return EXIT_FAILURE;
  }
  // Set opened NFC device to initiator mode
  if (nfc_initiator_init(pnd) < 0) {
    nfc_perror(pnd, "nfc_initiator_init");
    exit(EXIT_FAILURE);
  }

  printf("NFC reader: %s opened\n", nfc_device_get_name(pnd));
  printf("...\n", nfc_device_get_name(pnd));
  
  while (true){
    // Poll for a ISO14443A (MIFARE) tag
    const nfc_modulation nmMifare = {
      .nmt = NMT_ISO14443A,
      .nbr = NBR_106,
    };
    if (nfc_initiator_select_passive_target(pnd, nmMifare, NULL, 0, &nt) > 0) {
      print_hex(nt.nti.nai.abtUid, nt.nti.nai.szUidLen);
    }
    sleep(1);
  }
    
    // Close NFC device
  nfc_close(pnd);
  // Release the context
  nfc_exit(context);
  return EXIT_SUCCESS;
}
