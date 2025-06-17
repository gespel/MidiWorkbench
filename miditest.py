import pygame.midi
import time
import librosa

def list_midi_devices():
    pygame.midi.init()
    print("Verfügbare MIDI-Ausgabegeräte:")

    output_ids = []
    for i in range(pygame.midi.get_count()):
        interf, name, is_input, is_output, opened = pygame.midi.get_device_info(i)
        if is_output:
            output_ids.append(i)
            print(f"[{i}] {name.decode()}")

    return output_ids

def send_midi_sequence(device_id):
    player = pygame.midi.Output(device_id)
    print(f"Sende Sequenz an Gerät {device_id}")
    notes = [note_to_midi_nr("c3"), note_to_midi_nr("d3"), note_to_midi_nr("c#3")]
    print(notes)

    while True:
        print("Sending")
        for note in notes:
            player.note_on(note, velocity=100)
            time.sleep(0.1)
            player.note_off(note, velocity=100)
    player.close()

def note_to_midi_nr(note):
    return int(librosa.note_to_midi(note))

    

if __name__ == "__main__":
    devices = list_midi_devices()
    if not devices:
        print("Keine MIDI-Ausgabegeräte gefunden.")
    else:
        device_id = devices[1]
        send_midi_sequence(device_id)

    pygame.midi.quit()